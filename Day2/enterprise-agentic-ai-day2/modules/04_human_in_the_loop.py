from pathlib import Path

from src.approval_store import get_pending_approvals, resolve_approval, submit_for_approval
from src.config import RISK_APPROVAL_THRESHOLD
from src.enterprise_tools import (
    TOOL_DEFINITIONS,
    calculate_risk_score,
    check_credit_score,
    execute_tool_with_trace,
    screen_sanctions_list,
)
from src.foundry_client import ask_ai, ask_ai_with_tools
from src.simple_retriever import retrieve_context
from src.trace_logger import log_trace
from src.workflow_engine import SupplierOnboardingWorkflow, SupplierRequest


def main():
    module = "04_human_in_the_loop"

    request = SupplierRequest(
        supplier_id="SUP-2026-0311",
        legal_name="Emerald Global Trading LLC",
        country="AE",
        category="Raw Materials",
        annual_spend_usd=750000,
        contact_email="compliance@emeraldglobal.example",
        notes="High spend supplier with limited trading history",
    )

    workflow = SupplierOnboardingWorkflow(request)

    log_trace(module, "Orchestrator", "Workflow started", "SUCCESS", request.supplier_id)
    workflow.advance("Intake validated")

    credit = check_credit_score(request.legal_name, request.country)
    sanctions = screen_sanctions_list(request.legal_name, request.country)
    risk = calculate_risk_score(
        credit_score=credit["credit_score"],
        sanctions_match=sanctions["match_found"],
        spend_usd=request.annual_spend_usd,
    )

    workflow.context.artifacts["credit"] = credit
    workflow.context.artifacts["sanctions"] = sanctions
    workflow.context.artifacts["risk"] = risk
    workflow.advance("Due diligence completed")

    chunks = retrieve_context("high spend supplier approval and human review requirements", top_k=3)
    policy_context = "\n\n".join([
        f"Source: {doc['source']}\n{doc['content']}"
        for doc in chunks
    ])

    policy_answer = ask_ai(
        system_prompt=Path("prompts/compliance_rag_agent.txt").read_text(encoding="utf-8"),
        user_prompt=f"Supplier: {request.legal_name}\n\nPolicy Context:\n{policy_context}",
        feature=module,
    )

    workflow.context.artifacts["policy_review"] = policy_answer
    workflow.advance("Policy check completed")

    risk_score = risk["risk_score"]
    workflow.route_after_risk(risk_score=risk_score, threshold=RISK_APPROVAL_THRESHOLD)

    final_status = "PENDING"

    if workflow.context.state.value == "HUMAN_REVIEW":
        approval_id = submit_for_approval(
            supplier_id=request.supplier_id,
            legal_name=request.legal_name,
            risk_score=risk_score,
            reason="High spend and elevated risk score require procurement manager approval",
        )

        pending = get_pending_approvals()
        log_trace(module, "ApprovalQueue", "Pending item created", "SUCCESS", f"approval_id={approval_id}; pending={len(pending)}")

        review_summary = f"""
        Supplier: {request.legal_name}
        Risk Score: {risk_score}
        Credit: {credit}
        Sanctions: {sanctions}
        Policy Review: {policy_answer}
        """

        human_decision = ask_ai(
            system_prompt=Path("prompts/human_reviewer.txt").read_text(encoding="utf-8"),
            user_prompt=review_summary,
            feature=module,
        )

        approved = "APPROVE" in human_decision.upper()
        resolve_approval(approval_id, approved=approved, reviewer="regional_procurement_manager")
        workflow.complete(approved=approved, detail="Human reviewer decision captured")
        final_status = "APPROVED" if approved else "REJECTED"

        print("\nHuman Reviewer Output:\n")
        print(human_decision)

    else:
        tool_summary = ask_ai_with_tools(
            system_prompt=Path("prompts/due_diligence_agent.txt").read_text(encoding="utf-8"),
            user_prompt=f"Auto-approve and register supplier {request.legal_name}",
            tools=TOOL_DEFINITIONS,
            tool_executor=lambda name, args: execute_tool_with_trace(name, args, feature=module),
            feature=module,
        )
        workflow.complete(approved=True, detail="Auto-approved")
        final_status = "AUTO_APPROVED"

        print("\nAuto Approval Path:\n")
        print(tool_summary)

    print("\n===== Human-in-the-Loop Workflow Demo =====\n")
    print(workflow.summary())
    print(f"\nFinal Status: {final_status}")
    print(f"Risk Threshold Used: {RISK_APPROVAL_THRESHOLD}")


if __name__ == "__main__":
    main()

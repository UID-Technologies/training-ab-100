from pathlib import Path

from src.trace_logger import log_trace
from src.workflow_engine import SupplierOnboardingWorkflow, SupplierRequest


def main():
    module = "01_workflow_automation"

    request = SupplierRequest(
        supplier_id="SUP-2026-0142",
        legal_name="Nordic Components Global AB",
        country="SE",
        category="Industrial Fasteners",
        annual_spend_usd=420000,
        contact_email="vendor.onboarding@nordiccomponents.example",
        notes="Strategic supplier for APAC plant expansion",
    )

    workflow = SupplierOnboardingWorkflow(request)

    log_trace(module, "WorkflowEngine", "Input received", "SUCCESS", request.legal_name)
    workflow.advance("Supplier intake form validated")

    workflow.context.artifacts["kyc_status"] = "Documents uploaded"
    log_trace(module, "WorkflowEngine", "Due diligence", "SUCCESS", "KYC package complete")
    workflow.advance("KYC package complete")

    workflow.context.artifacts["policy_scope"] = "Enhanced verification required (>250k spend)"
    log_trace(module, "WorkflowEngine", "Policy check", "SUCCESS", "Policy scope determined")
    workflow.advance("Policy scope determined")

    workflow.context.artifacts["preliminary_risk"] = 58
    log_trace(module, "WorkflowEngine", "Risk scoring", "SUCCESS", "Preliminary risk calculated")

    print("\n===== Workflow Automation Demo =====\n")
    print(workflow.summary())
    print("\nArtifacts:")
    for key, value in workflow.context.artifacts.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()

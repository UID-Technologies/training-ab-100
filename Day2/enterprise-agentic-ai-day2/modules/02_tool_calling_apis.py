from pathlib import Path

from src.enterprise_tools import TOOL_DEFINITIONS, execute_tool_with_trace
from src.foundry_client import ask_ai_with_tools
from src.trace_logger import log_trace


def main():
    module = "02_tool_calling_apis"

    supplier_context = """
    New supplier onboarding request:
    - Supplier ID: SUP-2026-0199
    - Legal Name: Pacific Global Industrial Ltd
    - Country: SG
    - Category: Precision Machinery
    - Expected Annual Spend: USD 680,000

    Perform due diligence using enterprise APIs and recommend next action.
    """

    system_prompt = Path("prompts/due_diligence_agent.txt").read_text(encoding="utf-8")

    log_trace(module, "DueDiligenceAgent", "Started", "SUCCESS", "Tool calling workflow started")

    answer = ask_ai_with_tools(
        system_prompt=system_prompt,
        user_prompt=supplier_context,
        tools=TOOL_DEFINITIONS,
        tool_executor=lambda name, args: execute_tool_with_trace(name, args, feature=module),
        feature=module,
    )

    log_trace(module, "DueDiligenceAgent", "Completed", "SUCCESS", answer[:500])

    print("\n===== Tool Calling and APIs Demo =====\n")
    print(answer)


if __name__ == "__main__":
    main()

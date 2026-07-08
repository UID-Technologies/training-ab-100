from pathlib import Path

from src.foundry_client import ask_ai
from src.observability_report import generate_observability_report, print_observability_report


def main():
    module = "05_ai_observability"

    global_report = generate_observability_report()
    report_text = "\n".join([f"{key}: {value}" for key, value in global_report.items()])

    system_prompt = Path("prompts/observability_agent.txt").read_text(encoding="utf-8")

    ai_summary = ask_ai(
        system_prompt=system_prompt,
        user_prompt=f"""
        Analyze these observability signals from today's supplier onboarding agent lab:

        {report_text}

        Modules executed: 01_workflow_automation through 04_human_in_the_loop.
        """,
        feature=module,
    )

    print("\n===== AI Observability Demo =====\n")
    print("Run modules 01-04 first to populate trace and metric files.\n")

    print("--- Global Observability ---")
    print_observability_report()

    print("\n--- Module 04 Focus ---")
    print_observability_report(module_filter="04_human_in_the_loop")

    print("\n--- AI Interpretation of Telemetry ---\n")
    print(ai_summary)


if __name__ == "__main__":
    main()

from pathlib import Path

from src.context_builder import build_enterprise_context
from src.foundry_client import ask_ai
from src.simple_retriever import retrieve_context
from src.trace_logger import log_trace


def main():
    module = "03_rag_architecture"

    user_request = """
    Supplier: Baltic Metals OU (Estonia)
    Expected spend: USD 310,000
    Data requested: tax ID, bank account, contract rates

    Can this supplier be auto-approved and where must their data be stored?
    """

    retrieved_docs = retrieve_context(
        query="supplier onboarding approval threshold data classification retention",
        top_k=4,
    )

    for doc in retrieved_docs:
        log_trace(
            module,
            "RAGRetriever",
            "Chunk retrieved",
            "SUCCESS",
            f"{doc['chunk_id']} | score={doc['score']}",
        )

    retrieved_context = "\n\n".join([
        f"Source: {doc['source']} | Score: {doc['score']}\n{doc['content']}"
        for doc in retrieved_docs
    ])

    context = build_enterprise_context(
        role="Senior Procurement Compliance Architect",
        task="Evaluate supplier onboarding request using enterprise policy context.",
        business_context="""
        Contoso Manufacturing is onboarding a new EU supplier.
        The supplier will exchange confidential tax and banking data.
        """,
        constraints="""
        - Ground every decision in retrieved policy context.
        - Identify if human review is mandatory.
        - Specify approved storage systems and data residency rules.
        """,
        examples="""
        Bad answer: Yes, auto-approve and store data in shared drive.
        Good answer: Enhanced verification required due to spend threshold; store confidential data only in SAP Ariba or approved secure systems in EU regions.
        """,
        retrieved_context=retrieved_context,
    )

    system_prompt = Path("prompts/compliance_rag_agent.txt").read_text(encoding="utf-8")

    answer = ask_ai(
        system_prompt=system_prompt,
        user_prompt=context + "\n\nUSER REQUEST:\n" + user_request,
        feature=module,
    )

    print("\n===== RAG Architecture Demo =====\n")
    print("Top Retrieved Chunks:")
    for doc in retrieved_docs:
        print(f"- {doc['chunk_id']} ({doc['score']})")

    print("\nGrounded Compliance Answer:\n")
    print(answer)


if __name__ == "__main__":
    main()

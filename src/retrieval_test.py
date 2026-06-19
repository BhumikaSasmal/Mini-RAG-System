import os
from src.vector_store import VectorStore
from src.embedding_service import EmbeddingService


def run_retrieval_test():

    os.makedirs("outputs", exist_ok=True)

    output_path = "outputs/retrieval_test_results.md"

    embedder = EmbeddingService()

    store = VectorStore(
        collection_name="documents",
        persist_dir="vector_store/chroma"
    )

    queries = [
        {
            "query": "What is the purpose of a sample policy?",
            "expected": "Purpose or introduction section"
        },
        {
            "query": "Why is communication important in a policy?",
            "expected": "Communication responsibilities section"
        },
        {
            "query": "What does the document say about definitions of key terms?",
            "expected": "Definitions or terminology section"
        },
        {
            "query": "What are the review and update requirements?",
            "expected": "Review or maintenance section"
        },
        {
            "query": "Who is responsible for policy enforcement?",
            "expected": "Roles or enforcement section"
        },
        {
            "query": "Summarize the overall document",
            "expected": "General overview content"
        }
    ]

    markdown_lines = []

    markdown_lines.append("# Retrieval Test Results\n")

    for test_case in queries:

        query = test_case["query"]
        expected = test_case["expected"]

        print("\n" + "=" * 60)
        print("Query:", query)

        query_embedding = embedder.embed_text(query)

        results = store.query(
            query_embedding=query_embedding,
            top_k=3
        )

        markdown_lines.append(f"## Query\n")
        markdown_lines.append(f"{query}\n")

        markdown_lines.append("### Expected Match\n")
        markdown_lines.append(f"{expected}\n")

        if not results:

            print("No results found.")

            markdown_lines.append(
                "### Result\nNo results found.\n"
            )

            markdown_lines.append("---\n")

            continue

        markdown_lines.append("### Retrieved Results\n")

        for i, result in enumerate(results):

            metadata = result.get("metadata", {})

            text = result.get("text", "").strip()

            distance = result.get("score", 0)

            preview = text[:400]

            print(f"\nResult {i + 1}")
            print("Distance:", distance)
            print(preview)

            markdown_lines.append(
                f"#### Result {i + 1}\n"
            )

            markdown_lines.append(
                f"- Source File: {metadata.get('source_file')}\n"
            )

            markdown_lines.append(
                f"- Page Number: {metadata.get('page_number')}\n"
            )

            markdown_lines.append(
                f"- Chunk Index: {metadata.get('chunk_index')}\n"
            )

            markdown_lines.append(
                f"- Distance Score: {distance}\n"
            )

            markdown_lines.append(
                "\n```text\n"
            )

            markdown_lines.append(
                f"{preview}\n"
            )

            markdown_lines.append(
                "```\n"
            )

        markdown_lines.append("---\n")

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write("\n".join(markdown_lines))

    print("\nSaved retrieval test results to:")
    print(output_path)


if __name__ == "__main__":
    run_retrieval_test()

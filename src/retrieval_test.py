from src.vector_store import VectorStore
from src.embedding_service import EmbeddingService


def run_retrieval_test():
    embedder = EmbeddingService()

    store = VectorStore(
        collection_name="documents",
        persist_dir="vector_store/chroma"
    )

    queries = [
        "What is this document about?",
        "Summarize the main topic",
        "What are the key points discussed?"
    ]

    for q in queries:
        print("\n" + "="*50)
        print("Query:", q)

        query_embedding = embedder.embed_text(q)

        results = store.collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )

        docs = results.get("documents", [[]])[0]

        for i, doc in enumerate(docs):
            print(f"\nResult {i+1}:")
            print(doc[:300])  


if __name__ == "__main__":
    run_retrieval_test()

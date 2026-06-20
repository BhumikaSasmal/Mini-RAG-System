from src.vector_store import VectorStore
from src.llm_service import LLMService

class RAGPipeline:

    def __init__(self):
        self.store = VectorStore()
        self.llm = LLMService()

    def retrieve_chunks(
        self,
        question,
        top_k=3
    ):
        return self.store.query(
            query_text=question,
            top_k=top_k
        )

    def build_context(
        self,
        retrieved_chunks
    ):
        context_parts = []

        for result in retrieved_chunks:

            text = result.get(
                "text",
                ""
            ).strip()

            if text:
                context_parts.append(text)

        return "\n\n".join(context_parts)

    def format_sources(
        self,
        retrieved_chunks
    ):
        sources = []

        for result in retrieved_chunks:

            metadata = result.get(
                "metadata",
                {}
            )

            page_number = metadata.get(
                "page_number"
            )

            if page_number == -1:
                page_number = "N/A"

            sources.append({
                "source_file":
                    metadata.get("source_file"),
                "file_type":
                    metadata.get("file_type"),
                "page_number":
                    page_number,
                "chunk_id":
                    metadata.get("chunk_id"),
                "chunk_index":
                    metadata.get("chunk_index")
            })

        return sources

    def answer_question(
        self,
        question,
        top_k=3
    ):
        retrieved_chunks = self.retrieve_chunks(
            question,
            top_k=top_k
        )
        RELEVANCE_THRESHOLD = 1.5

        filtered_chunks = [
            chunk
            for chunk in retrieved_chunks
            if chunk.get("score", 999) < RELEVANCE_THRESHOLD
        ]

        context = self.build_context(
            filtered_chunks
        )

        answer = self.llm.generate_answer(
            question,
            context
        )
        sources = self.format_sources(
            retrieved_chunks
        )

        return {
            "question": question,
            "answer": answer,
            "sources": sources,
            "retrieval_results":
                retrieved_chunks
        }
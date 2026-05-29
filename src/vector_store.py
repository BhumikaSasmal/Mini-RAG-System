import chromadb

from src.embedding_service import EmbeddingService
from src.config import (
    COLLECTION_NAME,
    PERSIST_DIR
)

class VectorStore:
    def __init__(
        self,
        collection_name=COLLECTION_NAME,
        persist_dir=PERSIST_DIR
    ):
        self.client = chromadb.PersistentClient(path=persist_dir)

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

        self.embedder = EmbeddingService()

    def add_chunks(self, chunks):
        if not chunks:
            raise ValueError("No chunks provided for indexing.")

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk in chunks:

            if not isinstance(chunk, dict):
                continue

            text = chunk.get("text", "").strip()

            if not text:
                continue

            embedding = chunk.get("embedding")

            if embedding is None:
                continue

            chunk_id = chunk.get("chunk_id")

            if not chunk_id:
                continue

            ids.append(chunk_id)

            documents.append(text)

            embeddings.append(embedding)

            page_number = chunk.get("page_number")

            if page_number == "N/A":
                page_number = None

            page_number = chunk.get("page_number")

            metadata = {
                "source_file": str(chunk.get("source_file", "")),
                "file_type": str(chunk.get("file_type", "")),
                "page_number": page_number if page_number is not None else -1,
                "chunk_index": int(chunk.get("chunk_index", 0)),
                "char_count": int(chunk.get("char_count", 0))
            }

            metadatas.append(metadata)

        if not ids:
            raise ValueError(
                "No valid chunks found. Check chunk text and embeddings."
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def reset_collection(self):
        name = self.collection.name

        self.client.delete_collection(name)

        self.collection = self.client.get_or_create_collection(
            name=name
        )

    def count(self):
        return self.collection.count()

    def query(
        self,
        query_text=None,
        query_embedding=None,
        top_k=3
    ):
        if query_embedding is None:

            if not query_text or not query_text.strip():
                raise ValueError(
                    "Query text or query embedding is required."
                )

            query_embedding = self.embedder.embed_text(query_text)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        output = []

        if not results or not results.get("documents"):
            return output

        for i in range(len(results["documents"][0])):

            output.append({
                "text": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "score": results["distances"][0][i]
            })

        return output

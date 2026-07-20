from src.embedding_service import EmbeddingService
from src.vector_store import VectorStore
from src.config import (
    COLLECTION_NAME,
    PERSIST_DIR
)


def run_indexing(chunks, reset=False):

    if not chunks:
        return {
            "added": 0,
            "total": 0
        }

    valid_chunks = []

    for chunk in chunks:

        if not isinstance(chunk, dict):
            continue

        text = chunk.get("text", "").strip()

        if not text:
            continue

        valid_chunks.append(chunk)

    if not valid_chunks:
        return {
            "added": 0,
            "total": 0
        }

    embedder = EmbeddingService()

    texts = [
        chunk["text"]
        for chunk in valid_chunks
    ]

    embeddings = embedder.embed_texts(texts)

    for chunk, embedding in zip(valid_chunks, embeddings):
        chunk["embedding"] = embedding

    store = VectorStore(
        collection_name=COLLECTION_NAME,
        persist_dir=PERSIST_DIR
    )

    if reset:
        store.reset_collection()

    added = store.add_chunks(valid_chunks)

    return {
        "added": added,
        "total": store.count()
    }

from src.embedding_service import EmbeddingService
from src.vector_store import VectorStore
from src.config import (
    COLLECTION_NAME,
    PERSIST_DIR
)


def run_indexing(chunks):

    if not chunks:
        return 0

    valid_chunks = []

    for chunk in chunks:

        if not isinstance(chunk, dict):
            continue

        text = chunk.get("text", "").strip()

        if not text:
            continue

        valid_chunks.append(chunk)

    if not valid_chunks:
        return 0

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

    store.reset_collection()

    store.add_chunks(valid_chunks)

    return store.count()

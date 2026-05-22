from src.chunking import process_chunks
from src.embedding_service import EmbeddingService
from src.vector_store import VectorStore
import fitz  

def load_file(file_path):
    records = []
    doc = fitz.open(file_path)

    for i, page in enumerate(doc):
        text = page.get_text()

        if text.strip():
            records.append({
                "text": text,
                "source_file": file_path,
                "file_type": "pdf",
                "page_number": i + 1
            })

    return records

def run_indexing(records):
    chunks, _ = process_chunks(records)

    embedder = EmbeddingService()
    texts = [c["text"] for c in chunks]
    embeddings = embedder.embed_texts(texts)

    for c, e in zip(chunks, embeddings):
        c["embedding"] = e

    store = VectorStore(
        collection_name="documents",
        persist_dir="vector_store/chroma"
    )

    store.reset_collection()
    store.add_chunks(chunks)

    print("Indexed chunks:", store.count())


if __name__ == "__main__":
    records1= load_file("data/sample_docs/sample_policy.txt")
    run_indexing(records1)
    records2= load_file("data/sample_docs/sample_report.pdf")
    run_indexing(records2)

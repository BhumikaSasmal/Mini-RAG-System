import chromadb


class VectorStore:
    def __init__(self, collection_name="documents", persist_dir="vector_store/chroma"):
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def add_chunks(self, chunks):
        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk in chunks:
            ids.append(chunk["chunk_id"])
            documents.append(chunk["text"])
            embeddings.append(chunk["embedding"])

            metadata = {
                "source_file": chunk["source_file"],
                "file_type": chunk["file_type"],
                "page_number": chunk["page_number"],
                "chunk_index": chunk["chunk_index"],
                "char_count": chunk["char_count"]
            }

            metadatas.append(metadata)

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def reset_collection(self):
        name = self.collection.name
        self.client.delete_collection(name)
        self.collection = self.client.get_or_create_collection(name=name)

    def count(self):
        return self.collection.count()
    def query(self, query_text, top_k=3):
        results = self.collection.query(
            query_texts=[query_text],
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

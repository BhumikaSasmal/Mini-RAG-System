from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text):
        embedding = self.model.encode(text)
        return embedding.tolist()

    def embed_texts(self, texts):
        embeddings = self.model.encode(texts)
        return [e.tolist() for e in embeddings]

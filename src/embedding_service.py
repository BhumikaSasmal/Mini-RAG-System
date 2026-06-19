from sentence_transformers import SentenceTransformer

from src.config import EMBEDDING_MODEL_NAME


_model_instance = None


def get_embedding_model(model_name=EMBEDDING_MODEL_NAME):
    global _model_instance

    if _model_instance is None:
        _model_instance = SentenceTransformer(model_name)

    return _model_instance


class EmbeddingService:
    def __init__(self, model_name=EMBEDDING_MODEL_NAME):
        self.model = get_embedding_model(model_name)

    def embed_text(self, text):
        embedding = self.model.encode(text)
        return embedding.tolist()

    def embed_texts(self, texts):
        embeddings = self.model.encode(texts)
        return [e.tolist() for e in embeddings]

import os

CHUNK_SIZE = 180
CHUNK_OVERLAP = 40
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "documents"
PERSIST_DIR = "vector_store/chroma"

RELEVANCE_THRESHOLD = 1.5
TOP_K_RESULTS = 3

LLM_MODE = os.getenv("LLM_MODE", "mock").lower()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "gemini-3.6-flash")

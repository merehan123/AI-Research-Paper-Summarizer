from langchain_ollama import OllamaEmbeddings
from src.utils.config import EMBEDDING_MODEL

def load_embedding_model() -> OllamaEmbeddings:
    """
    Load the embedding model used for RAG.
    """
    return OllamaEmbeddings(model=EMBEDDING_MODEL)


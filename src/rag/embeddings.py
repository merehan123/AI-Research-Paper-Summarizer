from langchain_ollama import OllamaEmbeddings
from src.utils.config import EMBEDDING_MODEL

def load_embedding_model() -> OllamaEmbeddings:
    """
    Load the embedding model used for RAG.
    """
    return OllamaEmbeddings(model=EMBEDDING_MODEL)


def create_embedding(text: str) -> list[float]:
    """
    Create an embedding vector for a single text.
    """
    embedding_model = load_embedding_model()
    return embedding_model.embed_query(text)
from langchain_community.vectorstores import FAISS

def create_vector_store(
    chunks: list[str],
    embedding_model,
):
    """
    Create a FAISS vector store from text chunks.
    """

    return FAISS.from_texts(
        texts=chunks,
        embedding=embedding_model,
    )
def retrieve_context(
    query: str,
    vector_store,
    k: int = 3,
) -> str:
    """
    Retrieve the most relevant chunks from the FAISS vector store.
    """

    docs = vector_store.similarity_search(query, k=k)

    if not docs:
        return ""

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    return context
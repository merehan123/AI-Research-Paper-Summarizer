from src.llm.model import generate_response
from src.llm.prompts import CONCEPTS_PROMPT
from src.rag.retriever import retrieve_context


def explain_concepts(
    user_request: str,
    vector_store,
    k: int = 3,
) -> str:
    """
    Explain a concept using the most relevant retrieved context.
    """

    context = retrieve_context(
        query=user_request,
        vector_store=vector_store,
        k=k,
    )

    if not context:
        return "The requested concept is not discussed in the provided paper."

    prompt = CONCEPTS_PROMPT.format(
        question=user_request,
        paper=context,
    )

    return generate_response(
        prompt,
        temperature=0.2,
        max_tokens=500,
    )
from src.llm.model import generate_response
from src.llm.prompts import QA_PROMPT
from src.rag.retriever import retrieve_context


def answer_question(
    question: str,
    vector_store,
    k: int = 3,
) -> str:
    """
    Answer a question using the retrieved context from the paper.
    """

    context = retrieve_context(
        query=question,
        vector_store=vector_store,
        k=k,
    )

    if not context:
        return "I couldn't find this information in the uploaded paper."

    prompt = QA_PROMPT.format(
        context=context,
        question=question,
    )

    return generate_response(
        prompt,
        temperature=0,
        max_tokens=200,
    )
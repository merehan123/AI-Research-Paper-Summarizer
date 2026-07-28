from src.llm.model import generate_response
from src.llm.prompts import CONCEPTS_PROMPT


def explain_concepts(
    user_request: str,
    paper_text: str,
) -> str:
    """
    Explain a concept from the research paper.
    """

    prompt = CONCEPTS_PROMPT.format(
        question=user_request,
        paper=paper_text,
    )

    return generate_response(
        prompt,
        temperature=0.2,
        max_tokens=500,
    )
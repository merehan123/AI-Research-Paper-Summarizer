from src.llm.model import generate_response
from src.llm.prompts import SUMMARY_PROMPT


def generate_summary(paper_text: str) -> str:
    """
    Generate a structured summary of the research paper.
    """

    prompt = SUMMARY_PROMPT.format(
        paper=paper_text
    )

    return generate_response(
        prompt,
        temperature=0.2,
        max_tokens=700,
    )
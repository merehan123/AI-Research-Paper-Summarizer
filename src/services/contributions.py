from src.llm.model import generate_response
from src.llm.prompts import CONTRIBUTIONS_PROMPT


def extract_contributions(paper_text: str) -> str:
    """
    Extract the original contributions claimed by the research paper.
    """

    prompt = CONTRIBUTIONS_PROMPT.format(
        paper=paper_text
    )

    return generate_response(
        prompt,
        temperature=0.2,
        max_tokens=500
    )
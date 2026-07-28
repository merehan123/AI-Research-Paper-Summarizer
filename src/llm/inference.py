from src.llm.model import generate_response
from src.llm.prompts import ROUTER_PROMPT


def classify_request(user_query: str) -> str:
    """
    Classify the user's request into one of the supported intents.
    """

    prompt = ROUTER_PROMPT.format(query=user_query)

    intent = generate_response(
        prompt,
        temperature=0.1,
        max_tokens=10,
    )

    return intent.strip().upper()
from src.llm.model import generate_response
from src.llm.prompts import ROUTER_PROMPT

VALID_INTENTS = {"SUMMARY", "CONTRIBUTIONS", "CONCEPTS", "QUESTION", "GREETING"}


def classify_request(user_query: str) -> str:
    """
    Classify the user's request into one of the supported intents.

    If the underlying model call failed (e.g. Ollama unreachable),
    the raw error message is returned instead of a silent
    "unable to classify" fallback, so the real cause is visible.
    """

    prompt = ROUTER_PROMPT.format(query=user_query)

    raw_response = generate_response(
        prompt,
        temperature=0.1,
        max_tokens=10,
    )

    if raw_response.strip().startswith("⚠️"):
        return raw_response

    intent = raw_response.strip().upper()

    if intent not in VALID_INTENTS:
        return "QUESTION"

    return intent
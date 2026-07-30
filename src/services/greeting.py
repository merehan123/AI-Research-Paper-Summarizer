from src.llm.model import generate_response
from src.llm.prompts import GREETING_PROMPT


def greeting(user_request: str) -> str:
    dynamic_prompt = (
        f"{GREETING_PROMPT}\n\n"
        f"User message: {user_request}\n"
    )

    return generate_response(
        dynamic_prompt,
        temperature=0.9,
        max_tokens=50,
    )
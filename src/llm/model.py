from src.utils.config import LLM_MODEL
import ollama

# Create a reusable function to generate responses using the Qwen model


def generate_response(
    prompt: str,
    temperature: float = 0.3,
    max_tokens: int = 1024
) -> str:
    """
    Generate a response using the Qwen model through Ollama.

    Args:
        prompt: The input prompt for the LLM.
        temperature: Controls randomness of the generated response.
        max_tokens: Maximum number of tokens to generate.

    Returns:
        The generated text response.
    """

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": temperature,
            "num_predict": max_tokens
        }
    )

    return response["message"]["content"]
from src.utils.config import LLM_MODEL
import ollama


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
        The generated text response, or a user-facing error message
        if the model call fails.
    """

    try:
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

    except ollama.ResponseError as e:
        return f"⚠️ The AI model returned an error: {e.error}"

    except (ConnectionError, TimeoutError):
        return (
            "⚠️ Couldn't reach the Ollama server. "
            "Make sure it's running (`ollama serve`)."
        )

    except Exception as e:
        return f"⚠️ Unexpected error while generating a response: {e}"
from src.utils.config import LLM_MODEL
import ollama


def generate_response(
    prompt: str,
    temperature: float = 0.3,
    max_tokens: int = 1024,
    num_ctx: int = 8192,
) -> str:
    """
    Generate a response using the Qwen model through Ollama.

    Args:
        prompt: The input prompt for the LLM.
        temperature: Controls randomness of the generated response.
        max_tokens: Maximum number of tokens to generate.
        num_ctx: Context window size in tokens. Ollama defaults to
            2048, which silently truncates long papers — raised
            here so full-paper prompts aren't cut off.

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
                "num_predict": max_tokens,
                "num_ctx": num_ctx,
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
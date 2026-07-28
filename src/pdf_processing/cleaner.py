import re
import unicodedata

# Clean Text
def clean_pdf_text(page_text: str) -> str:
    """
    Clean extracted PDF text for RAG applications.

    Steps:
    1. Normalize Unicode characters.
    2. Remove page break characters.
    3. Fix hyphenated words split across lines.
    4. Remove tabs.
    5. Remove isolated page numbers.
    6. Strip extra whitespace from each line.
    7. Collapse multiple spaces.
    8. Collapse excessive blank lines.
    """

    text = unicodedata.normalize("NFKC", page_text)
    text = text.replace("\x0c", "")
    text = text.replace("\t", " ")
    text = re.sub(r"(\w+)-\s*\n\s*(\w+)", r"\1\2", text)
    lines = [line.strip() for line in text.split("\n")]
    lines = [line for line in lines if line]

    lines = [
        line for line in lines
        if not re.match(r'^(page\s*)?\d+\s*$', line, re.IGNORECASE)
    ]

    text = "\n".join(lines)
    text = re.sub(r"[ ]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()

# Remove References
def remove_references(text: str) -> str:
    """
    Remove the References section and everything after it.
    """

    pattern = r"\n\s*(\d+\.?\s*)?references\b.*"

    cleaned = re.sub(
        pattern,
        "",
        text,
        flags=re.IGNORECASE | re.DOTALL
    )

    return cleaned
import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from all pages of a PDF.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        The extracted text as a single string.
    """
    if not pdf_path.lower().endswith(".pdf"):
        raise ValueError("Invalid file format. Only PDF files are supported.")

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    page_count = len(document)

    title = document.metadata.get("title", "").strip()

    if not title:
        for line in text.splitlines():
            if line.strip():
                title = line.strip()
                break

    return text, title, page_count
import fitz  # PyMuPDF


class PDFExtractionError(Exception):
    """Raised when a PDF cannot be opened or read."""


def extract_text_from_pdf(pdf_path: str) -> tuple[str, str, int]:
    """
    Extract text from all pages of a PDF.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        A (text, title, page_count) tuple.

    Raises:
        PDFExtractionError: if the file isn't a valid, readable,
        text-based PDF.
    """

    if not pdf_path.lower().endswith(".pdf"):
        raise PDFExtractionError("Invalid file format. Only PDF files are supported.")

    try:
        document = fitz.open(pdf_path)
    except Exception as e:
        raise PDFExtractionError(f"Couldn't open the PDF file: {e}") from e

    try:
        ...
        return text, title, page_count
    finally:
        document.close()
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
        if document.is_encrypted:
            raise PDFExtractionError(
                "This PDF is password-protected and can't be read."
            )

        text = ""
        for page in document:
            text += page.get_text()

        if not text.strip():
            raise PDFExtractionError(
                "No extractable text found in this PDF — it might be a "
                "scanned image without OCR."
            )

        page_count = len(document)
        title = document.metadata.get("title", "").strip()

        if not title:
            for line in text.splitlines():
                if line.strip():
                    title = line.strip()
                    break

        return text, title, page_count

    finally:
        document.close()
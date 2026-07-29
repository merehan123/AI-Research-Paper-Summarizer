import os
import pytest
import fitz

from src.pdf_processing.extractor import extract_text_from_pdf, PDFExtractionError

SAMPLE_DIR = os.path.join("data", "sample_papers")


def sample_pdfs():
    if not os.path.isdir(SAMPLE_DIR):
        return []
    return [
        os.path.join(SAMPLE_DIR, f)
        for f in os.listdir(SAMPLE_DIR)
        if f.lower().endswith(".pdf")
    ]


@pytest.mark.parametrize("pdf_path", sample_pdfs())
def test_extracts_nonempty_text_from_real_papers(pdf_path):
    text, title, page_count = extract_text_from_pdf(pdf_path)
    assert text.strip() != ""
    assert page_count > 0
    assert isinstance(title, str)


def test_rejects_non_pdf_extension(tmp_path):
    fake_file = tmp_path / "notes.txt"
    fake_file.write_text("just some text")

    with pytest.raises(PDFExtractionError, match="Invalid file format"):
        extract_text_from_pdf(str(fake_file))


def test_raises_on_empty_pdf(tmp_path):
    empty_pdf_path = tmp_path / "empty.pdf"

    doc = fitz.open()
    doc.new_page()
    doc.save(str(empty_pdf_path))
    doc.close()

    with pytest.raises(PDFExtractionError, match="No extractable text"):
        extract_text_from_pdf(str(empty_pdf_path))


def test_raises_on_corrupted_pdf(tmp_path):
    corrupted_path = tmp_path / "broken.pdf"
    corrupted_path.write_bytes(b"%PDF-1.4 not a real pdf structure")

    with pytest.raises(PDFExtractionError):
        extract_text_from_pdf(str(corrupted_path))
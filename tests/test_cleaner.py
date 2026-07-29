from src.pdf_processing.cleaner import clean_pdf_text, remove_references


def test_removes_page_break_characters():
    raw = "Page one text\x0cPage two text"
    cleaned = clean_pdf_text(raw)
    assert "\x0c" not in cleaned


def test_joins_hyphenated_words_split_across_lines():
    raw = "This is a hyphen-\nated word."
    cleaned = clean_pdf_text(raw)
    assert "hyphenated" in cleaned


def test_removes_isolated_page_numbers():
    raw = "Some content.\n42\nMore content."
    cleaned = clean_pdf_text(raw)
    assert "42" not in cleaned.splitlines()


def test_collapses_multiple_blank_lines():
    raw = "Line one.\n\n\n\n\nLine two."
    cleaned = clean_pdf_text(raw)
    assert "\n\n\n" not in cleaned


def test_collapses_multiple_spaces():
    raw = "Too    many     spaces here."
    cleaned = clean_pdf_text(raw)
    assert "  " not in cleaned


def test_remove_references_strips_trailing_section():
    text = "Intro text.\n\nReferences\n[1] Some citation."
    cleaned = remove_references(text)
    assert "citation" not in cleaned
    assert "Intro text." in cleaned


def test_remove_references_keeps_body_before_it():
    text = "Section 1: Method.\nSection 2: Results.\nReferences\n[1] X."
    cleaned = remove_references(text)
    assert "Method" in cleaned
    assert "Results" in cleaned


def test_remove_references_false_positive_on_section_heading():
    """
    Known limitation: if a body section heading starts with the
    word "References" (even if it's not the bibliography, e.g. a
    section titled "References to Prior Systems"), the regex still
    cuts everything from that line onward. This test documents the
    current behavior so a future fix is verifiable.
    """
    text = (
        "Section 3: Related Work.\n"
        "References to Prior Systems\n"
        "This section is actual body content, not the bibliography."
    )
    cleaned = remove_references(text)
    assert "actual body content" not in cleaned
    assert "Related Work" in cleaned
from src.pdf_processing.splitter import split_into_chunks


def test_returns_list_of_strings():
    text = "word " * 500
    chunks = split_into_chunks(text, chunk_size=200, chunk_overlap=50)
    assert isinstance(chunks, list)
    assert all(isinstance(c, str) for c in chunks)


def test_produces_multiple_chunks_for_long_text():
    text = "word " * 500
    chunks = split_into_chunks(text, chunk_size=200, chunk_overlap=50)
    assert len(chunks) > 1


def test_no_chunk_exceeds_requested_size_by_much():
    text = "word " * 500
    chunk_size = 200
    chunks = split_into_chunks(text, chunk_size=chunk_size, chunk_overlap=50)
    assert all(len(c) <= chunk_size + 20 for c in chunks)


def test_short_text_returns_single_chunk():
    text = "This is a short paper abstract."
    chunks = split_into_chunks(text, chunk_size=1000, chunk_overlap=200)
    assert len(chunks) == 1
    assert chunks[0] == text


def test_empty_text_returns_empty_list():
    chunks = split_into_chunks("", chunk_size=1000, chunk_overlap=200)
    assert chunks == []


def test_consecutive_chunks_overlap():
    text = "sentence " * 300
    chunks = split_into_chunks(text, chunk_size=300, chunk_overlap=100)
    assert len(chunks) > 1
    overlap_found = chunks[0][-30:] in chunks[1]
    assert overlap_found
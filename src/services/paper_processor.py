from src.pdf_processing.extractor import extract_text_from_pdf
from src.pdf_processing.cleaner import (clean_pdf_text,remove_references)
from src.pdf_processing.splitter import split_into_chunks
from src.rag.embeddings import load_embedding_model
from src.rag.vector_store import create_vector_store

def process_pdf(pdf_path: str):
    """
    Process a PDF and build the FAISS vector store.
    """

    text, title, page_count = extract_text_from_pdf(pdf_path)

    text = clean_pdf_text(text)

    text = remove_references(text)

    chunks = split_into_chunks(text)

    embedding_model = load_embedding_model()

    vector_store = create_vector_store(
        chunks,
        embedding_model,
    )

    return text, chunks, vector_store, title, page_count
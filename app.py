import os
import time
import streamlit as st

from src.services.paper_processor import process_pdf
from src.pdf_processing.extractor import PDFExtractionError
from src.main import research_assistant
from src.utils.config import (
    LLM_MODEL,
    EMBEDDING_MODEL,
)

st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📄",
    layout="wide",
)

st.title("📄 AI Research Paper Assistant")
st.caption("Upload a research paper and chat with it using AI.")

if "paper_title" not in st.session_state:
    st.session_state.paper_title = ""

if "page_count" not in st.session_state:
    st.session_state.page_count = 0

if "word_count" not in st.session_state:
    st.session_state.word_count = 0

if "messages" not in st.session_state:
    st.session_state.messages = []

if "paper_loaded" not in st.session_state:
    st.session_state.paper_loaded = False

if "paper_text" not in st.session_state:
    st.session_state.paper_text = ""

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = ""

quick_prompt = None

uploaded_file = st.file_uploader(
        "Upload PDF",
        type="pdf"
    )

with st.sidebar:
    st.subheader("📄 Paper Information")

    if st.session_state.paper_loaded:

        st.success("PDF Loaded")

        st.write(f"**Title:** {st.session_state.paper_title}")

        st.write(f"**Pages:** {st.session_state.page_count}")

        st.write(f"**Words:** {st.session_state.word_count:,}")

        st.write(f"**Chunks:** {len(st.session_state.chunks)}")

        st.divider()

        st.subheader("🚀 Quick Actions")

        if st.button("📝 Summarize", use_container_width=True):
            quick_prompt = "Summarize this paper"

        if st.button("⭐ Contributions", use_container_width=True):
            quick_prompt = "What are the main contributions of this paper?"

        if st.button("💡 Explain Method", use_container_width=True):
            quick_prompt = "Explain the methodology used in this paper."

        if st.button("📊 Dataset", use_container_width=True):
            quick_prompt = "What dataset was used in this paper?"

    st.divider()

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


if uploaded_file is not None:

    if (
        not st.session_state.paper_loaded
        or uploaded_file.name != st.session_state.pdf_name
    ):

        os.makedirs("uploads", exist_ok=True)

        path = os.path.join(
            "uploads",
            uploaded_file.name.replace(" ", "_")
        )

        with open(path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            with st.spinner("Processing PDF..."):

                start = time.time()

                paper_text, chunks, vector_store, title, page_count = process_pdf(path)

                end = time.time()

        except PDFExtractionError as e:
            st.error(f"❌ {e}")
            st.stop()

        except Exception as e:
            st.error(f"❌ Unexpected error while processing the PDF: {e}")
            st.stop()

        st.session_state.paper_loaded = True
        st.session_state.paper_text = paper_text
        st.session_state.vector_store = vector_store
        st.session_state.chunks = chunks
        st.session_state.pdf_name = uploaded_file.name
        st.session_state.paper_title = title
        st.session_state.page_count = page_count
        st.session_state.word_count = len(paper_text.split())

        st.success(
            f"✅ {uploaded_file.name} loaded successfully "
            f"({end-start:.2f} sec)"
        )
        st.rerun()


if st.session_state.paper_loaded:

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    typed_prompt = st.chat_input(
        "Ask anything about the paper...",
        key="chat_box"
    )

    prompt = quick_prompt if quick_prompt else typed_prompt

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                start = time.time()

                response = research_assistant(
                    user_request=prompt,
                    paper_text=st.session_state.paper_text,
                    vector_store=st.session_state.vector_store,
                )

                end = time.time()

            st.markdown(response)

            st.caption(
                f"{end-start:.2f} sec"
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

if st.session_state.messages:

    history = ""

    for msg in st.session_state.messages:

        history += (
            f"{msg['role'].upper()}:\n"
            f"{msg['content']}\n\n"
        )

    st.download_button(
        "⬇ Download Conversation",
        history,
        file_name="conversation.txt",
    )
import time

from src.services.paper_processor import process_pdf
from src.main import research_assistant

print("🚀 Starting project...")

pdf_path = "data/sample_papers/rag.pdf"

print("📄 Processing PDF...")
start = time.time()

paper_text, chunks, vector_store = process_pdf(pdf_path)

print(f"✅ PDF processed in {time.time() - start:.2f} seconds")
print(f"📑 Number of chunks: {len(chunks)}")

query = "Summarize this paper"

print("🤖 Sending request to the LLM...")

start = time.time()

response = research_assistant(
    user_request=query,
    paper_text=paper_text,
    vector_store=vector_store,
)

print(f"✅ Response generated in {time.time() - start:.2f} seconds")

print("\n========== RESPONSE ==========\n")
print(response)
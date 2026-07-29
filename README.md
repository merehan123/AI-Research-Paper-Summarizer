# 📚 AI Research Paper Assistant

An AI-powered application that helps students and researchers quickly understand academic papers using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).

---

## 📖 Overview

Reading research papers is often time-consuming and challenging due to their technical language and length.

This project allows users to upload a research paper in PDF format, automatically extracts its content, generates concise summaries, identifies the main contributions, explains difficult technical concepts in simple language, and answers user questions based on the uploaded paper.

The system combines document processing, semantic retrieval, and large language models to provide accurate and context-aware responses.

---

## 🎯 Objectives

- Automatically summarize research papers.
- Extract the key contributions of a paper.
- Explain technical concepts in simple language.
- Answer questions about uploaded research papers.
- Improve reading efficiency for students and researchers.

---

## ✨ Features

### 📄 PDF Upload

Upload any academic paper in PDF format.

### 📝 Text Extraction

Extract text using PyMuPDF.

### 🧹 Text Preprocessing

- Clean extracted text
- Remove unnecessary spaces
- Remove empty lines
- Split long documents into chunks

### 🔎 Semantic Search (RAG)

- Generate embeddings
- Store embeddings in FAISS
- Retrieve the most relevant document chunks

### 🤖 AI-Powered Summarization

Generate concise summaries using a Large Language Model.

### 📌 Key Contributions Extraction

Identify the main contributions and findings of the paper.

### 💡 Technical Concept Explanation

Explain complex scientific terms in simple language.

### ❓ Question Answering

Allow users to ask questions related to the uploaded paper using Retrieval-Augmented Generation (RAG).

---

# 🏗️ System Architecture

```
                  User
                    │
                    ▼
             Upload PDF
                    │
                    ▼
          PDF Text Extraction
                    │
                    ▼
           Text Cleaning
                    │
                    ▼
          Text Chunking
                    │
                    ▼
        Sentence Embeddings
                    │
                    ▼
            FAISS Index
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
  Summarization          Question Answering
         │                     │
         └──────────┬──────────┘
                    ▼
             Large Language Model
                    │
                    ▼
             Streamlit Interface
```

---

# 📂 Project Structure

```
AI-Research-Paper-Summarizer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── sample_papers/
│
├── uploads/
│
├── notebooks/
│
├── docs/
│
└── src/
    ├── pdf_processing/
    ├── llm/
    ├── rag/
    ├── services/
    └── utils/
```

---

# 🧠 Technologies

## Programming Language

- Python

## User Interface

- Streamlit

## PDF Processing

- PyMuPDF

## Large Language Model

- Qwen 2.5 Instruct

## Embedding Model

- Sentence Transformers

## Vector Database

- FAISS

## Deep Learning Framework

- PyTorch

## NLP Libraries

- Hugging Face Transformers

---

# ⚙️ Workflow

1. Upload a research paper.
2. Extract text from the PDF.
3. Clean and preprocess the extracted text.
4. Split the document into chunks.
5. Generate embeddings for each chunk.
6. Store embeddings in a FAISS vector database.
7. Generate:
   - Summary
   - Key Contributions
   - Technical Explanations
8. Answer user questions using Retrieval-Augmented Generation (RAG).
9. Display all results through the Streamlit interface.

---

# 📦 Modules

## PDF Processing

- Text Extraction
- Text Cleaning
- Text Chunking

## LLM Layer

- Model Loading
- Prompt Management
- Text Generation

## RAG Layer

- Embeddings
- FAISS
- Retriever

## AI Services

- Summarization
- Contributions Extraction
- Technical Explanation
- Question Answering

## Frontend

- Streamlit User Interface
- Pipeline Integration

---

# 📸 Screenshots

Coming Soon...

---

# 🚀 Future Improvements

- Multi-document support
- OCR support for scanned PDFs
- Citation generation
- Automatic keyword extraction
- Research paper comparison
- Chat history
- Multi-language support
- Export summaries to PDF

---

# 👥 Team Members

| Name | Responsibility |
|------|----------------|
| Member 1 | PDF Processing |
| Member 2 | LLM Integration |
| Member 3 | RAG Pipeline |
| Member 4 | AI Services |
| Member 5 | Frontend & Pipeline Integration |

---

# 📄 License

This project was developed for educational purposes as part of an AI/NLP course.

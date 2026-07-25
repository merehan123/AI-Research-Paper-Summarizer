# Project Architecture

## Overview

The project follows a modular architecture where each module has a single responsibility.

```
                    Streamlit UI
                         │
                         ▼
                     app.py
                         │
        ┌────────────────────────────────────┐
        │                                    │
        ▼                                    ▼
 PDF Processing                       AI Services
        │                                    │
        ▼                                    ▼
      RAG -------------------------> LLM Layer
        │                                    │
        └────────────────────────────────────┘
                         │
                         ▼
                    Display Results
```

---

# Modules

## 1. User Interface

Responsible for:

- Uploading PDFs
- Displaying summaries
- Displaying explanations
- Displaying chat
- Receiving user questions

Files

```
app.py
```

---

## 2. PDF Processing

Responsible for converting a PDF into clean text.

Files

```
extractor.py
cleaner.py
splitter.py
```

Responsibilities

- Extract text
- Clean text
- Split into chunks

Input

PDF

Output

Chunks

---

## 3. RAG Layer

Responsible for retrieving the most relevant information.

Files

```
embeddings.py

vector_store.py

retriever.py
```

Responsibilities

- Generate embeddings
- Build FAISS index
- Retrieve relevant chunks

Input

Chunks

Output

Relevant Context

---

## 4. LLM Layer

Responsible for interacting with Qwen.

Files

```
model.py

prompts.py

inference.py
```

Responsibilities

- Load model
- Store prompts
- Generate responses

Input

Prompt

Output

Generated Text

---

## 5. Services Layer

Contains the business logic.

Files

```
summarizer.py

contributions.py

explanation.py

qa_service.py
```

Responsibilities

- Generate summary
- Extract contributions
- Explain concepts
- Answer questions

---

## 6. Utilities

Contains helper functions and configuration.

Files

```
config.py

helpers.py
```

---

# Why This Architecture?

- Modular
- Easy to maintain
- Easy to test
- Easy for teamwork
- Supports parallel development
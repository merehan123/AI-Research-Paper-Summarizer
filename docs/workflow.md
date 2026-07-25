# Project Workflow

## Step 1

The user uploads a research paper in PDF format.

```
User
    │
    ▼
Upload PDF
```

---

## Step 2

The uploaded PDF is saved temporarily.

```
uploads/
```

---

## Step 3

Text Extraction

The PDF is opened using PyMuPDF.

```
PDF

↓

Raw Text
```

---

## Step 4

Cleaning

The extracted text is cleaned.

Operations

- Remove empty lines
- Remove extra spaces
- Remove page numbers

Output

```
Clean Text
```

---

## Step 5

Chunking

The document is divided into smaller chunks.

```
Clean Text

↓

Chunk 1

Chunk 2

Chunk 3

...
```

---

## Step 6

Embedding Generation

Each chunk is converted into a vector representation.

```
Chunk

↓

Sentence Transformer

↓

Embedding
```

---

## Step 7

Vector Store

All embeddings are stored in FAISS.

```
Embeddings

↓

FAISS Index
```

---

## Step 8

Summary Generation

The complete paper is sent to the LLM with the summary prompt.

Output

- Objective
- Methodology
- Results
- Conclusion

---

## Step 9

Key Contributions

The LLM extracts the most important contributions.

Output

```
•

•

•

•
```

---

## Step 10

Technical Explanation

The LLM explains difficult concepts using simple language.

Example

Transformer

↓

Simple explanation

---

## Step 11

Question Answering

The user asks a question.

```
Question

↓

Embedding

↓

Retriever

↓

Relevant Chunks

↓

Prompt

↓

Qwen

↓

Answer
```

---

## Step 12

Display Results

The Streamlit interface displays

- Summary
- Contributions
- Explanation
- Chat

```
User
     │
     ▼
Streamlit
```
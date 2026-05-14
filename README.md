# enterprise-rag-assistant
Enterprise-grade retrieval-augmented generation (RAG) ai assistant using LangChain, FAISs, FastAPI, and LLM.
# Enterprise RAG Assistant

AI-powered Enterprise Knowledge Assistant built using FastAPI, FAISS, Sentence Transformers, and Retrieval-Augmented Generation (RAG) architecture.

---

# Features

- Upload PDF documents
- Extract text from PDFs
- Chunk large documents
- Generate embeddings using Sentence Transformers
- Store embeddings in FAISS Vector Database
- Retrieve relevant chunks using semantic similarity
- Ask questions from uploaded documents
- FastAPI backend APIs
- Modular production-style architecture

---

# Tech Stack

- Python
- FastAPI
- FAISS
- Sentence Transformers
- LangChain Text Splitters
- Uvicorn

---

# Project Structure

```bash
enterprise-rag-assistant/
│
├── app/
│   ├── api/
│   ├── rag/
│   ├── services/
│   ├── models/
│   ├── database/
│   └── core/
│
├── data/
├── screenshots/
├── notebooks/
├── requirements.txt
├── main.py
└── README.md

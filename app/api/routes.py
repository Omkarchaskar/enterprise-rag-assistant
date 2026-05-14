from fastapi import APIRouter, UploadFile, File
from app.services.pdf_loader import load_pdf
from app.rag.chunking import chunk_text
from app.rag.embeddings import create_embeddings
from app.rag.vector_store import create_vector_store
from app.rag.retrieval import retrieve_relevant_chunks
from app.services.llm_service import generate_answer
import os
router = APIRouter()

# Globla  storage. atta global vapru production chya veles use karycha nasto apan!
global_vector_store = None
global_chunks = None


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    global global_vector_store
    global global_chunks

    # Create uploads folder
    os.makedirs("data/raw_docs", exist_ok=True)

    file_path = f"data/raw_docs/{file.filename}"

    # Save uploaded PDF
    with open(file_path, "wb") as pdf_file:
        pdf_file.write(await file.read())

    # Extract text karun ghetla PDF madhun
    extracted_text = load_pdf(file_path)

    # Create chunks kele
    chunks = chunk_text(extracted_text)

    # Generate embeddings karun ghetle chunks sathi
    embeddings = create_embeddings(chunks)

    # Store vector DB globally for retrieval during question answering so easy padel aplyala
    global_vector_store = create_vector_store(embeddings)
    global_chunks = chunks

    return {
        "filename": file.filename,
        "total_chunks": len(chunks),
        "message": "PDF processed successfully"
    }


@router.post("/ask")
async def ask_question(question: str):

    global global_vector_store
    global global_chunks

    if global_vector_store is None:
        return {
            "error": "Please upload a PDF first"
        }

    # Retrieve relevant chunks , question vr adharit 
    retrieved_chunks = retrieve_relevant_chunks(
        question,
        global_vector_store,
        global_chunks
    )

    # Generat kru  AI answer
    answer = generate_answer(
        question,
        retrieved_chunks
    )

    return {
        "question": question,
        "answer": answer,
        "retrieved_chunks": retrieved_chunks
    }
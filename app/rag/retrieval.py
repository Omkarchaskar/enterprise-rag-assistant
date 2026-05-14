import numpy as np
from sentence_transformers import SentenceTransformer


embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve_relevant_chunks(
    query,
    vector_store,
    chunks,
    top_k=3
):
    """
    Retrieve most relevant chunks
    """

    # Convert question into embedding
    query_embedding = embedding_model.encode([query])

    # Search FAISS index
    distances, indices = vector_store.search(
        np.array(query_embedding),
        top_k
    )

    # Get relevant chunks
    retrieved_chunks = []

    for index in indices[0]:
        retrieved_chunks.append(chunks[index])

    return retrieved_chunks
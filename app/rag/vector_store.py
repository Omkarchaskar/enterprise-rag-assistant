import faiss
import numpy as np


def create_vector_store(embeddings):
    """
    Store embeddings inside FAISS vector DB
    """

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index
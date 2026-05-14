from sentence_transformers import SentenceTransformer


embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_embeddings(chunks):
    """
    Convert text chunks into embeddings
    """

    embeddings = embedding_model.encode(chunks)

    return embeddings
import requests


def generate_answer(question, context_chunks):

    context = "\n\n".join(context_chunks)

    prompt = f"""
    You are an AI assistant.

    Answer the question only using
    the provided context.

    Context:
    {context}

    Question:
    {question}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    return result["response"]
from groq import Groq

from backend.rag import get_chunks

from backend.vectordb import (
    create_vector_db,
    search_chunks
)

client = Groq(
    api_key="API_KEY"
)

chunks = []
index = None


def rebuild_rag(pdf_path):
    global chunks
    global index

    chunks = get_chunks(pdf_path)

    index = create_vector_db(chunks)


def ask_gemini(question):

    global chunks
    global index

    if index is None:
        return "Please upload a PDF first."

    context = search_chunks(
        question,
        chunks,
        index
    )

    prompt = f"""
Answer ONLY from the provided context.

Context:
{context}

Question:
{question}

If answer is not found, reply:
Answer not found in document.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
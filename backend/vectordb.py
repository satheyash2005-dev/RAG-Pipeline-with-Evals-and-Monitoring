from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_vector_db(chunks):
    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings).astype("float32"))

    return index


def search_chunks(question, chunks, index, k=3):

    query_embedding = model.encode([question])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        k
    )

    result = []

    for i in indices[0]:
        result.append(chunks[i])

    return "\n".join(result)
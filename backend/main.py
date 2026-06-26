from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

from backend.llm import ask_gemini,rebuild_rag

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    question: str


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    content = await file.read()

    with open(file_path, "wb") as f:
        f.write(content)

    print("Saved:", file_path)
    print("Size:", os.path.getsize(file_path))

    rebuild_rag(file_path)

    return {
        "message": "PDF uploaded successfully"
    }


@app.post("/ask")
def ask(data: Question):

    answer = ask_gemini(data.question)

    return {
        "answer": answer
    }
# 📄 RAG Pipeline with Evals and Monitoring

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions based on their content. The project uses vector embeddings for document retrieval and the Groq LLM for generating accurate, context-aware responses.

---

## 🚀 Features

- 📂 Upload PDF documents
- ✂️ Automatic text chunking
- 🔍 Semantic search using vector database
- 🤖 Llama 3.3 (Groq API) integration
- 💬 Context-aware Question Answering
- 📊 RAG pipeline with evaluation and monitoring
- 🌐 Simple web interface

---

## 🛠️ Tech Stack

- Python
- FastAPI
- HTML
- CSS
- JavaScript
- FAISS
- Sentence Transformers
- Groq API (Llama 3.3)

---

## 📁 Project Structure

```
RAG-Project/
│── backend/
│   ├── llm.py
│   ├── rag.py
│   ├── vectordb.py
│   ├── main.py
│
│── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│
│── uploads/
│── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/satheyash2005-dev/RAG-Pipeline-with-Evals-and-Monitoring.git
```

Go to the project folder

```bash
cd RAG-Pipeline-with-Evals-and-Monitoring
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## ▶️ Run the Project

```bash
python backend/main.py
```

Open your browser and visit

```
http://127.0.0.1:8000
```

---

## 📖 How It Works

1. Upload a PDF.
2. The document is split into chunks.
3. Chunks are converted into vector embeddings.
4. Relevant chunks are retrieved using semantic search.
5. The retrieved context is passed to the Groq Llama model.
6. The model generates an answer based only on the uploaded document.

---

## 📷 Screenshots

Add screenshots of your application here.

---

## 📌 Future Improvements

- Support multiple PDFs
- Chat history
- Authentication
- Better evaluation metrics
- Docker deployment
- Cloud deployment (Render/AWS)

---


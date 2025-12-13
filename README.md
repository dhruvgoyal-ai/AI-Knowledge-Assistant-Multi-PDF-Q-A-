# 🤖 Personal AI Knowledge Assistant

A personal AI chatbot that answers questions from your own documents using RAG.

## 🚀 Features
- Document-based question answering
- Fast vector search using FAISS
- Local LLM using Ollama (Phi-3)
- Simple Streamlit UI
- FastAPI backend

## 🛠 Tech Stack
- Python 3.11
- FastAPI
- LangChain
- FAISS
- Streamlit
- Ollama (Phi-3)

## 📂 Project Structure
backend/ - API & RAG logic
frontend/ - Streamlit UI
data/ - Upload PDFs


## ▶️ How to Run

### 1. Create virtual environment
```bash
python -m venv venv

2. Activate venv
.\venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Create vector database
python backend/ingest.py

5. Run backend
uvicorn backend.main:app --reload

6. Run frontend
streamlit run frontend/app.py
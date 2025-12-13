from fastapi import FastAPI
from backend.rag import ask_question

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.post("/chat")
def chat(query: str):
    answer = ask_question(query)
    return {"answer": answer}

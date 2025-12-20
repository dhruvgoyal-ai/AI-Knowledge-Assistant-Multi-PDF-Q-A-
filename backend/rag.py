from ingest import get_vectorstore
from langchain_community.llms import Ollama

llm = Ollama(model="phi3:mini")

def get_answer(session_id, question):
    # ❌ No session → no PDF
    if not session_id:
        return "❌ Please upload a PDF first."

    vectorstore = get_vectorstore(session_id)

    # ❌ No vectorstore → no PDF
    if vectorstore is None:
        return "❌ Please upload a PDF first."

    # 🔍 Deep search for large PDFs
    docs = vectorstore.similarity_search(question, k=15)

    if not docs:
        return "❌ Answer not found in the uploaded PDF."

    # 🧹 Extra safety filter (optional but good)
    filtered_docs = [
        d for d in docs
        if len(d.page_content.strip()) > 100
    ]

    if not filtered_docs:
        return "❌ Answer not found in the uploaded PDF."

    context = "\n".join(d.page_content for d in filtered_docs)

    prompt = f"""
You must answer ONLY using the PDF content below.
If the answer is not present in the PDF, say:
"Answer not found in the uploaded PDF."

PDF Content:
{context}

Question:
{question}
"""

    # ✅ CORRECT way to call Ollama
    response = llm.invoke(prompt)
    return response

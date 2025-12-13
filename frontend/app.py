import streamlit as st
import requests

st.set_page_config(page_title="Personal AI Assistant", page_icon="🤖")

st.title("🤖 Personal AI Knowledge Assistant")
st.write("Ask questions from your PDFs (OS, Maths, etc.)")

query = st.text_input("Ask a question")

if st.button("Ask"):
    if query.strip() == "":
        st.warning("Please enter a question")
    else:
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            params={"query": query}
        )
        st.success(response.json()["answer"])

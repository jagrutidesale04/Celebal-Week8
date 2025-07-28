import streamlit as st
from utils import load_loan_data, convert_to_text
from rag_pipeline import build_faiss_index, retrieve
from llm_generator import generate_answer
import os

st.title("💬 Loan Dataset RAG Q&A Bot")

if not os.path.exists("embeddings/faiss.index"):
    df = load_loan_data()
    docs = convert_to_text(df)
    build_faiss_index(docs)
    st.success("FAISS index built successfully!")

query = st.text_input("Ask a question about the dataset:")

if query:
    chunks = retrieve(query)
    context = "\n".join(chunks)
    answer = generate_answer(query, context)
    st.markdown("### 🤖 Answer")
    st.write(answer)

    with st.expander("🔍 Retrieved Context"):
        st.write(context)

# RAG Q&A Chatbot - Loan Approval Dataset

This chatbot uses Retrieval-Augmented Generation to answer questions based on a loan approval dataset using OpenAI or HuggingFace LLMs.

## Features
- Load and preprocess dataset
- Embed using Sentence Transformers
- Retrieve with FAISS
- Answer with OpenAI GPT or HuggingFace model
- Streamlit-based UI

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

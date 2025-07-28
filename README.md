# Week 8: RAG Q&A Chatbot

This project is part of **Week 8** of the **Celebal Summer Internship** program.

The objective of this task is to build a **RAG (Retrieval-Augmented Generation)** Q&A Chatbot. It combines document retrieval with generative AI to provide intelligent, context-aware responses from unstructured data sources.

## Objectives

- Implement a Retrieval-Augmented Generation (RAG) pipeline
- Retrieve relevant documents from vector store using similarity search
- Generate responses using a lightweight Hugging Face model or available LLM (OpenAI, Claude, Grok, Gemini)
- Deploy the chatbot locally using a web interface

## Features

- **Embedding Models**: SentenceTransformers (e.g., `all-MiniLM-L6-v2`)
- **Vector Store**: FAISS
- **LLM Used**: 
  - OpenAI GPT (with `.env` for secure API key usage) **or**
  - Hugging Face Transformers (for local inference using smaller models)
- **Document Loader**: PyMuPDF or PDFLoader
- **Interface**: Streamlit-based local web app
- **Environment**: Python 3.10+

## File Structure

```
rag-chatbot-loan/
├── app.py                     # Streamlit UI
├── rag_pipeline.py           # Core RAG implementation
├── utils.py                  # Helper functions
├── data/                     # Folder containing documents
├── .env                      # Contains API key for OpenAI
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/jagrutidesale04/rag-chatbot-loan.git
cd rag-chatbot-loan
```

### 2. Set up Environment

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
# or
source venv/bin/activate      # On macOS/Linux
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file

```
OPENAI_API_KEY=your_openai_api_key
```

### 5. Run Streamlit App

```bash
streamlit run app.py
```

## Requirements

```
openai
python-dotenv
faiss-cpu
sentence-transformers
PyMuPDF
langchain
streamlit
```

## Author

**Jagruti Desale**  
B.Tech – Data Science and Engineering (3rd Year)  
Summer Intern at Celebal Technologies

[GitHub](https://github.com/jagrutidesale04)  
[LinkedIn](https://www.linkedin.com/in/jagruti-desale-jd04)

## License

This project is intended for academic and learning purposes only as part of the Celebal Summer Internship Program.

from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle

def build_faiss_index(docs, index_path="embeddings/faiss.index", model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(docs, show_progress_bar=True)
    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    os.makedirs("embeddings", exist_ok=True)
    faiss.write_index(index, index_path)
    with open("embeddings/docs.pkl", "wb") as f:
        pickle.dump(docs, f)

def retrieve(query, k=5, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    query_embedding = model.encode([query])
    index = faiss.read_index("embeddings/faiss.index")
    with open("embeddings/docs.pkl", "rb") as f:
        docs = pickle.load(f)
    D, I = index.search(query_embedding, k)
    results = [docs[i] for i in I[0]]
    return results

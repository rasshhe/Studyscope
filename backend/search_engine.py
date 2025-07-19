# --- search_engine.py ---
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_answer_from_notes(question, subject, k=3, threshold=0.35):
    subject_path = f"subjects/{subject}"

    try:
        with open(f"{subject_path}/texts.pkl", "rb") as f:
            chunks = pickle.load(f)
        index = faiss.read_index(f"{subject_path}/faiss_index.pkl")
    except Exception as e:
        print(f"❌ Error loading subject data: {e}")
        return None

    query_embedding = model.encode([question], normalize_embeddings=True).astype("float32")
    distances, indices = index.search(query_embedding, k=k)

    best_score = distances[0][0]
    best_index = indices[0][0]

    if best_score < threshold:
        print(f"❌ No good match (similarity {best_score:.2f}) for: {question}")
        return None

    matched_chunk = chunks[best_index]
    print(f"✅ Match (similarity {best_score:.2f}): {matched_chunk[:120]}...")
    return matched_chunk, best_score

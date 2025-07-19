# backend/pdf_utils.py
import fitz  # PyMuPDF
import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_pdf(file_obj):
    doc = fitz.open(stream=file_obj.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def chunk_text(text, chunk_size=300):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def upload_and_process_pdf(uploaded_file, subject):
    text = extract_text_from_pdf(uploaded_file)
    chunks = chunk_text(text)

    if not chunks:
        raise ValueError("No text extracted from the uploaded PDF.")

    subject_dir = os.path.join("subjects", subject)
    os.makedirs(subject_dir, exist_ok=True)

    texts_path = os.path.join(subject_dir, "texts.pkl")
    index_path = os.path.join(subject_dir, "faiss_index.pkl")

    # Save text chunks
    if os.path.exists(texts_path):
        with open(texts_path, "rb") as f:
            existing_chunks = pickle.load(f)
        chunks = existing_chunks + chunks

    with open(texts_path, "wb") as f:
        pickle.dump(chunks, f)

    # Encode and index
    embeddings = model.encode(chunks, normalize_embeddings=True)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, index_path)

    return len(chunks)

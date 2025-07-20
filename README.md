# StudyScope - AI-Powered Academic Assistant

## Overview
**StudyScope** is an AI-powered academic assistant designed to help students interact with their study material more efficiently. It enables users to upload lecture PDFs, extract insights, generate quizzes, search notes semantically, and track study progress — all in one streamlined platform.

This project integrates modern AI techniques with traditional study workflows to offer a personalized learning experience. It is built with modular backend architecture and a user-friendly Streamlit UI.

## Key Features

### 🧠 AI-Powered Study Tools
- **Semantic Search**: Ask questions and get relevant answers directly from your uploaded notes using FAISS and cosine similarity.
- **AI Quiz Generation**: Generate multiple-choice quizzes from your notes using HuggingFace’s FLAN-T5 model.

### 📂 Subject-wise Content Management
- Upload PDFs to subject-specific folders (`subjects/<subject_name>`)
- Automatically extract and process content on upload

### 🔍 Smart Search
- Vector-based semantic search to retrieve answers from notes
- Fallback to GPT when no relevant answer is found

### 🧾 Notes, Tasks & Burnout Tracking
- Create and manage notes and to-do lists per subject
- **Track daily study hours and burnout levels** using interactive sliders
- Visualize personal study patterns and avoid overexertion

### 🖥️ Streamlit UI
- Clean and intuitive layout
- Tabs for search, flashcards, tasks, quizzes, timers, and wellness tracking
- Responsive elements and customizable themes

## Technical Stack

- **Language**: Python 3.10+
- **Framework**: Streamlit
- **Libraries**: 
  - `FAISS` for semantic search
  - `SentenceTransformers` for embeddings
  - `HuggingFace Transformers` (FLAN-T5) for quiz generation
  - `OpenAI GPT` (fallback) for unanswerable queries
- **File Structure**:
- /subjects/ # Per-subject folders containing uploaded PDFs
/backend/
├── pdf_utils.py # PDF reading and note extraction
├── search_engine.py # FAISS-based search
├── quiz_generator.py # Quiz generation with T5
├── gpt_helper.py # GPT fallback for low-score queries
app.py # Streamlit frontend
requirements.txt

##Future Scope

-Switch to HNSW indexing for better scalability
-Add user login and cloud-based file storage
-Mobile-friendly frontend using React Native or Flutter
-Adaptive revision plans based on user performance
-GPT-4 based summarization and note condensation
-Dashboard analytics for study time and burnout history

Author
Rashi Raj
B.Tech Computer Science (AIML)
University of Petroleum and Energy Studies
[GitHub Profile](https://github.com/rasshhe)



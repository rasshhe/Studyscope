
from transformers import pipeline

# Lightweight and fast — ideal for local usage
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def get_gpt_response(question):
    try:
        result = qa_pipeline(question, max_new_tokens=100)
        answer = result[0]['generated_text'].strip()
        return answer if answer else "⚠️ The model did not generate a response."
    except Exception as e:
        return f"❌ Hugging Face error: {str(e)}"

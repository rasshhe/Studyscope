# --- quiz_generator.py ---
from transformers import pipeline
import random

quiz_model = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_quiz_from_notes(chunks, num_questions=5):
    selected = random.sample(chunks, min(num_questions, len(chunks)))
    quiz = []

    for text in selected:
        # Skip if text is too short or empty
        if len(text.strip()) < 50:
            continue

        prompt = f"""Generate a multiple choice question from this note:
{text}

Format as:
Question: <question>
Options: A) <option1> B) <option2> C) <option3> D) <option4>
Answer: <correct_option_letter>"""

        try:
            result = quiz_model(prompt, max_new_tokens=150, do_sample=False)[0]['generated_text'].strip()

            if "Question:" in result and "Options:" in result and "Answer:" in result:
                question = result.split("Question:")[1].split("Options:")[0].strip()
                options_line = result.split("Options:")[1].split("Answer:")[0].strip()
                answer_letter = result.split("Answer:")[1].strip().upper()

                options = []
                for prefix in ["A)", "B)", "C)", "D)"]:
                    if prefix in options_line:
                        part = options_line.split(prefix)[1].strip()
                        options.append(part)

                if len(options) == 4 and answer_letter in ["A", "B", "C", "D"]:
                    quiz.append({
                        "question": question,
                        "options": options,
                        "answer": answer_letter
                    })

        except Exception as e:
            print(f"⚠️ Quiz generation error: {e}")
            continue

    return quiz

from openai import OpenAI
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
print("DEBUG: OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(query, context):
    prompt = f"""
You are a helpful assistant. Based on the following data chunks, answer the question.

Context:
{context}

Question: {query}

Answer:
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

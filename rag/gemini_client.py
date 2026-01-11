import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch key from .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(context, question):
    prompt = f"""
You are a financial assistant.
Answer ONLY using the context below.
If the answer is not present, say "Not available in the current data".

Context:
{context}

Question:
{question}
"""
    response = model.generate_content(prompt)
    return response.text

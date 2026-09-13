import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set")

client = genai.Client(api_key=api_key)


def generate_insight(question: str, result):
    result_text = json.dumps(result, default=str)

    prompt = f"""
You are a data analysis assistant.

User question:
{question}

Query result:
{result_text}

Analyze the query result and provide a concise, useful insight.

Rules:
- Use only the information present in the query result.
- Do not invent facts.
- Mention important patterns or comparisons.
- Keep the response simple and easy to understand.
- Return plain text.
- Do not create a table.
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text.strip()
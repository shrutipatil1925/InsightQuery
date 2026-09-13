import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set")

client = genai.Client(api_key=api_key)


def generate_sql(question: str, schema: str):

    prompt = f"""
You are an SQL generation assistant.

Database schema:
{schema}

User question:
{question}

Generate a SQL query that answers the user's question.

Rules:
- Generate only SELECT queries.
- Use only tables and columns present in the schema.
- Do not use INSERT, UPDATE, DELETE, DROP, ALTER, CREATE or PRAGMA.
- Return only the SQL query.
- Do not use markdown code fences.
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text.strip()
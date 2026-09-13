from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.graph import graph


router = APIRouter()


class ChatRequest(BaseModel):
    database_name: str
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    state = {
        "database_name": request.database_name,
        "user_question": request.question,
        "retry_count": 0
    }

    result = graph.invoke(state)

    return {
        "question": request.question,
        "sql_query": result.get("sql_query"),
        "query_result": result.get("query_result"),
        "chart_type": result.get("chart_type"),
        "chart": result["chart"].to_json() if result.get("chart") else None,
        "insight": result.get("insight")
    }
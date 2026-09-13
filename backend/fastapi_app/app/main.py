from fastapi import FastAPI
from app.api.database import router as database_router
from app.api.chat import router as chat_router


app = FastAPI(
    title="InsightQuery API",
    description="AI-powered conversational data analaysis API",
    version="1.0.0"
)

app.include_router(
    database_router, prefix="/api/database", tags=["Database"]
)

app.include_router(chat_router, prefix="/api", tags=["Chat"])


@app.get("/")
def home():
    return {"message":"InsightQuery API is running"}

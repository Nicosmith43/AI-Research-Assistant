from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.core.config import settings
from backend.app.db.init_db import init_database
from backend.app.api.research import router as research_router
from backend.app.api.history import router as history_router

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    """Create database tables if they don't already exist."""
    init_database()


app.include_router(research_router)
app.include_router(history_router)


@app.get("/")
def root():
    return {
        "message": "AI Research Assistant API is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
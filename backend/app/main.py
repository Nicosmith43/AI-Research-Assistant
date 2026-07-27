from fastapi import FastAPI

from backend.app.core.config import settings
from backend.app.api.routes import router
from backend.app.api.research import router as research_router
from backend.app.api.history import router as history_router

app = FastAPI(
    title=settings.app_name,
    version="0.1.0"
)

app.include_router(router)
app.include_router(research_router)
app.include_router(history_router)


@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} API is running!"
    }
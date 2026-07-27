from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.models.research_history import ResearchHistory
from backend.app.repositories.research_repository import get_all_research

router = APIRouter()


@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    records = get_all_research(db)

    return [
        {
            "id": record.id,
            "query": record.query,
            "answer": record.answer,
        }
        for record in records
    ]
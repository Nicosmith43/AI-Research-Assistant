from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.models.history import HistoryResponse
from backend.app.repositories.research_repository import (
    get_all_research,
    get_research_by_id,
)

router = APIRouter()


@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    records = get_all_research(db)

    return [
        {
            "id": record.id,
            "query": record.query,
            "answer": record.answer,
            "source": record.source,
            "favorite": record.favorite,
            "created_at": record.created_at,
        }
        for record in records
    ]


@router.get(
    "/history/{research_id}",
    response_model=HistoryResponse,
)
def get_history_item(
    research_id: int,
    db: Session = Depends(get_db),
):
    research = get_research_by_id(db, research_id)

    if research is None:
        raise HTTPException(
            status_code=404,
            detail="Research not found",
        )

    return research
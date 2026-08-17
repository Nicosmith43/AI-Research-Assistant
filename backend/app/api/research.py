from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.models.research import (
    ResearchRequest,
    ResearchResponse,
)
from backend.app.services.research_service import research_service

router = APIRouter()


@router.post("/research", response_model=ResearchResponse)
def research(
    request: ResearchRequest,
    db: Session = Depends(get_db),
):
    result = research_service.generate_research(
        query=request.query,
        db=db,
    )

    research = result["research"]
    sources = result["sources"]

    return ResearchResponse(
        id=research.id,
        query=research.query,
        answer=research.answer,
        sources=sources,
    )
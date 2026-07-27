from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.models.research import (
    ResearchRequest,
    ResearchResponse,
)
from backend.app.services.research_service import generate_research

router = APIRouter()


@router.post("/research", response_model=ResearchResponse)
def research(
    request: ResearchRequest,
    db: Session = Depends(get_db),
    ):

    answer = generate_research(request.query, db)

    return ResearchResponse(
        query=request.query,
        answer=answer
    )
from fastapi import APIRouter

from backend.app.models.research import (
    ResearchRequest,
    ResearchResponse
)

from backend.app.services.research_service import generate_research


router = APIRouter()


@router.post("/research", response_model=ResearchResponse)
def research(request: ResearchRequest):

    answer = generate_research(request.query)

    return ResearchResponse(
        query=request.query,
        answer=answer
    )
from sqlalchemy.orm import Session

from backend.app.services.wikipedia_service import wikipedia_service
from backend.app.repositories.research_repository import (
    create_research,
)


class ResearchService:
    """
    Handles all research generation logic.
    """

    def generate_research(
        self,
        query: str,
        db: Session,
    ):
        answer = wikipedia_service.get_summary(query)

        research = create_research(
            db=db,
            query=query,
            answer=answer,
        )

        return research


research_service = ResearchService()
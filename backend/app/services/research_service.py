from sqlalchemy.orm import Session

from backend.app.providers.research_provider import research_provider
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
        answer = research_provider.generate(query)

        research = create_research(
            db=db,
            query=query,
            answer=answer,
        )

        return research


research_service = ResearchService()
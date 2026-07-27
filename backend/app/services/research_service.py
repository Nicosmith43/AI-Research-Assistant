from sqlalchemy.orm import Session

from backend.app.repositories.research_repository import create_research


def generate_research(query: str, db: Session) -> str:
    answer = f"Research generated for: {query}"

    create_research(
        db=db,
        query=query,
        answer=answer,
    )

    return answer
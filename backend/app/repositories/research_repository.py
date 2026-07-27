from sqlalchemy.orm import Session

from backend.app.models.research_history import ResearchHistory


def create_research(
    db: Session,
    query: str,
    answer: str,
    source: str = "local",
) -> ResearchHistory:
    record = ResearchHistory(
        query=query,
        answer=answer,
        source=source,
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


def get_all_research(db: Session):
    return db.query(ResearchHistory).all()
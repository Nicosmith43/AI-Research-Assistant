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

def get_research_by_id(
    db: Session,
    research_id: int,
):
    return(
        db.query(ResearchHistory)
        .filter(ResearchHistory.id == research_id)
        .first()
    )


def delete_research(
    db: Session,
    research: ResearchHistory,
):
    db.delete(research)
    db.commit()

def toggle_favorite(
    db: Session,
    research: ResearchHistory,
):

    research.favorite = not research.favorite

    db.commit()
    db.refresh(research)

    return research
    
from backend.app.db.database import Base, engine

from backend.app.models.research_history import ResearchHistory


def init_database():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_database()
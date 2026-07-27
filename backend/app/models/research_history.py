from sqlalchemy import Column, Integer, String, Text

from backend.app.db.database import Base


class ResearchHistory(Base):
    __tablename__ = "research_history"

    id = Column(Integer, primary_key=True, index=True)

    query = Column(String, nullable=False)

    answer = Column(Text, nullable=False)
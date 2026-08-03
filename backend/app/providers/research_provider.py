from sqlalchemy.orm import Session

from backend.app.services.openai_service import openai_service
from backend.app.services.wikipedia_service import wikipedia_service


class ResearchProvider:

    def generate(self, query: str) -> str:
        wiki_summary = wikipedia_service.get_summary(query)

        try:
            return openai_service.improve_research(
                query=query,
                wikipedia_summary=wiki_summary,
            )
        except Exception:
            return wiki_summary


research_provider = ResearchProvider()
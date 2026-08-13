from sqlalchemy.orm import Session

from backend.app.providers.openai_provider import openai_provider
from backend.app.providers.wikipedia_provider import wikipedia_provider
from backend.app.providers.arxiv_provider import arxiv_provider
from backend.app.repositories.research_repository import create_research


class ResearchService:
    """
    Handles all research generation logic.
    """

    def generate_research(
        self,
        query: str,
        db: Session,
    ):
        # Get information from Wikipedia
        wiki_summary = wikipedia_provider.get_summary(query)

        # Get relevant academic papers from arXiv
        arxiv_results = arxiv_provider.search(
            query,
            max_results=5,
        )

        # Prepare arXiv information for the AI
        arxiv_summary = "\n\n".join(
            [
                f"Title: {paper['title']}\n"
                f"Authors: {', '.join(paper['authors'])}\n"
                f"Summary: {paper['summary']}\n"
                f"URL: {paper['url']}"
                for paper in arxiv_results
            ]
        )

        # Ask OpenAI to improve the research using both sources
        try:
            answer = openai_provider.improve_research(
                query=query,
                wikipedia_summary=wiki_summary,
                arxiv_summary=arxiv_summary,
            )
        except Exception as e:
            print(f"Error improving research: {e}")
            answer = wiki_summary

        # Save the final answer
        research = create_research(
            db=db,
            query=query,
            answer=answer,
        )

        return research


research_service = ResearchService()
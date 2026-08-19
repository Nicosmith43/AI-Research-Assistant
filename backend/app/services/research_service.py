from sqlalchemy.orm import Session

from backend.app.providers.arxiv_provider import arxiv_provider
from backend.app.providers.wikipedia_provider import wikipedia_provider
from backend.app.providers.openai_provider import openai_provider
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
        wiki_result = wikipedia_provider.get_summary(query)
        wiki_summary = wiki_result["extract"] if wiki_result else None

        # Get relevant academic papers from arXiv
        arxiv_results = arxiv_provider.search(
            query,
            max_results=5,
        )

        # Build a list of sources for the API response
        sources = []

        if wiki_result:
            sources.append(
                {
                    "type": "wikipedia",
                    "title": wiki_result["title"],
                    "url": wiki_result["url"],
                }
            )

        for paper in arxiv_results:
            sources.append(
                {
                    "type": "arxiv",
                    "title": paper["title"],
                    "url": paper["url"],
                }
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

        # Ask OpenAI to improve the research
        try:
            answer = openai_provider.improve_research(
                query=query,
                wikipedia_summary=wiki_summary or "No Wikipedia article found.",
                arxiv_summary=arxiv_summary,
            )
        except Exception as e:
            print(f"Error improving research: {e}")
            answer = wiki_summary or "Unable to generate research for this query."

        # Save the final answer
        research = create_research(
            db=db,
            query=query,
            answer=answer,
            source="Wikipedia + arXiv",
        )

        return {
            "research": research,
            "sources": sources,
        }


research_service = ResearchService()
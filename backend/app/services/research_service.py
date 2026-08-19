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
        wiki_summary = wikipedia_provider.get_summary(query)

        # Get relevant academic papers from arXiv
        arxiv_results = arxiv_provider.search(
            query,
            max_results=5,
        )

        # Build a list of sources for the API response
        sources = []

        if wiki_summary:
            sources.append(
                {
                    "type": "wikipedia",
                    "title": query,
                    "url": (
                        "https://en.wikipedia.org/wiki/"
                        + query.replace(" ", "_")
                    ),
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
                wikipedia_summary=wiki_summary,
                arxiv_summary=arxiv_summary,
            )
        except Exception as e:
            print(f"Error improving research: {e}")

            if wiki_summary:
                answer = (
                    "AI synthesis was unavailable. "
                    "Here is the available Wikipedia information:\n\n"
                    + wiki_summary
                )
            else:
                answer = (
                    "Unable to generate research because the AI service "
                    "and Wikipedia source were unavailable."
                )

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
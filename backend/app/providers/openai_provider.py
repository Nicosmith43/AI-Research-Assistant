from openai import OpenAI

from backend.app.core.config import settings


class OpenAIProvider:
    """
    Generates research explanations using OpenAI.
    """

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def improve_research(
        self,
        query: str,
        wikipedia_summary: str,
        arxiv_summary: str,
    ) -> str:

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional research assistant. "
                        "Use the provided research sources to create "
                        "a concise explanation suitable for a college student."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Research Topic: {query}\n\n"
                        f"Wikipedia Summary:\n"
                        f"{wikipedia_summary}\n\n"
                        f"Academic Research from arXiv:\n"
                        f"{arxiv_summary}\n\n"
                        "Create a concise, accurate explanation "
                        "based on these sources."
                    ),
                },
            ],
        )

        return response.choices[0].message.content


openai_provider = OpenAIProvider()
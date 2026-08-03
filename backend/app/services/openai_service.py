from openai import OpenAI

from backend.app.core.config import settings


class OpenAIService:

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )
    
    def improve_research(
        self,
        query: str,
        wikipedia_summary: str,
    ) -> str:

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional research assistant."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Research Topic: {query}\n\n"
                        f"Wikipedia Summary:\n"
                        f"{wikipedia_summary}\n\n"
                        "Create a concise explanation suitable for a college student."
                    ),
                },
            ],
        )

        return response.choices[0].message.content

openai_service = OpenAIService()
import requests


class WikipediaService:

    BASE_URL = "https://en.wikipedia.org/api/rest_v1/page/summary"

    def get_summary(self, topic: str) -> str:
        # Properly indented inside the function
        topic = topic.replace(" ", "_")
        url = f"{self.BASE_URL}/{topic}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("extract", "No summary available.")
        except requests.RequestException:
            return "Unable to retrieve information from Wikipedia."


wikipedia_service = WikipediaService()
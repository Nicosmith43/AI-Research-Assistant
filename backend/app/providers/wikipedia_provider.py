import requests


class WikipediaProvider:
    """
    Retrieves research summaries from Wikipedia.
    """

    def get_summary(self, query: str) -> str:
        url = (
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            + requests.utils.quote(query)
        )

        try:
            response = requests.get(
                url,
                timeout=10,
                headers={
                    "User-Agent": "AI-Research-Assistant/0.1"
                },
            )

            if response.status_code != 200:
                return "Unable to retrieve information from Wikipedia."

            data = response.json()

            return data.get(
                "extract",
                "Unable to retrieve information from Wikipedia.",
            )

        except requests.RequestException:
            return "Unable to retrieve information from Wikipedia."


wikipedia_provider = WikipediaProvider()
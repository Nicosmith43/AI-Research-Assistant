import requests


class WikipediaProvider:
    """
    Retrieves research summaries from Wikipedia.
    """

    SEARCH_URL = "https://en.wikipedia.org/w/api.php"
    SUMMARY_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

    def _find_best_title(self, query: str) -> str | None:
        """
        Uses Wikipedia's search API to resolve a natural-language query
        into the title of the best-matching article.
        """
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "srlimit": 1,
            "format": "json",
        }

        response = requests.get(
            self.SEARCH_URL,
            params=params,
            timeout=10,
            headers={"User-Agent": "AI-Research-Assistant/0.1"},
        )

        if response.status_code != 200:
            return None

        results = response.json().get("query", {}).get("search", [])

        if not results:
            return None

        return results[0]["title"]

    def get_summary(self, query: str) -> dict | None:
        """
        Resolves the query to a real Wikipedia article and returns its
        title, extract text, and canonical URL. Returns None if no
        article could be found or retrieved.
        """
        try:
            title = self._find_best_title(query)

            if not title:
                return None

            response = requests.get(
                self.SUMMARY_URL + requests.utils.quote(title),
                timeout=10,
                headers={"User-Agent": "AI-Research-Assistant/0.1"},
            )

            if response.status_code != 200:
                return None

            data = response.json()
            extract = data.get("extract")

            if not extract:
                return None

            return {
                "title": data.get("title", title),
                "extract": extract,
                "url": data.get("content_urls", {})
                .get("desktop", {})
                .get(
                    "page",
                    f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}",
                ),
            }

        except requests.RequestException:
            return None


wikipedia_provider = WikipediaProvider()
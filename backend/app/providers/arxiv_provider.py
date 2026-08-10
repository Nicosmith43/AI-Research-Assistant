import arxiv


class ArxivProvider:
    """
    Searches arXiv for academic papers.
    """

    def search(self, query: str, max_results: int = 5):
        client = arxiv.Client(
            page_size=max_results,
            delay_seconds=3.0,
            num_retries=2,
        )

        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance,
        )

        results = []

        for result in client.results(search):
            results.append(
                {
                    "title": result.title,
                    "summary": result.summary,
                    "authors": [author.name for author in result.authors],
                    "published": result.published.isoformat(),
                    "url": result.entry_id,
                }
            )

        return results


arxiv_provider = ArxivProvider()
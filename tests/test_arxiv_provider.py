from backend.app.providers.arxiv_provider import arxiv_provider


def test_arxiv_search():
    results = arxiv_provider.search(
        "machine learning",
        max_results=2,
    )

    assert len(results) > 0
    assert "title" in results[0]
    assert "summary" in results[0]
    assert "authors" in results[0]
    assert "url" in results[0]
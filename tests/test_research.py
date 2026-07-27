from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_research_endpoint():
    response = client.post(
        "/research",
        json={
            "query": "What is artificial intelligence?"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["query"] == "What is artificial intelligence?"
    assert "Research generated for" in data["answer"]

def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
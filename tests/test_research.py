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
    assert len(data["answer"]) > 0


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"


def test_get_history():
    response = client.get("/history")

    assert response.status_code == 200


def test_invalid_history():
    response = client.get("/history/99999")

    assert response.status_code == 404


def test_toggle_favorite():
    response = client.post(
        "/research",
        json={
            "query": "Test favorite research"
        }
    )

    assert response.status_code == 200

    research_id = response.json()["id"]

    response = client.post(
        f"/history/{research_id}/favorite"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == research_id
    assert data["favorite"] is True


def test_delete_history():
    response = client.post(
        "/research",
        json={
            "query": "Test delete research"
        }
    )

    assert response.status_code == 200

    research_id = response.json()["id"]

    response = client.delete(
        f"/history/{research_id}"
    )

    assert response.status_code == 200

    response = client.get(
        f"/history/{research_id}"
    )

    assert response.status_code == 404

def test_toggle_favorite():
    response = client.post(
        "/research",
        json={
            "query": "Test favorite research"
        }
    )

    assert response.status_code == 200

    research_id = response.json()["id"]

    response = client.post(
        f"/history/{research_id}/favorite"
    )

    assert response.status_code == 200
    assert response.json()["favorite"] is True


def test_delete_history():
    response = client.post(
        "/research",
        json={
            "query": "Test delete research"
        }
    )

    assert response.status_code == 200

    research_id = response.json()["id"]

    response = client.delete(
        f"/history/{research_id}"
    )

    assert response.status_code == 200

    response = client.get(
        f"/history/{research_id}"
    )

    assert response.status_code == 404

def test_empty_research_query():
    response = client.post(
        "/research",
        json={
            "query": ""
        }
    )

    assert response.status_code == 422
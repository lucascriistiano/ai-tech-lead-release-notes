from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_generate_release_notes() -> None:
    payload = {
        "version": "v1.4.0",
        "from_date": "2026-01-01",
        "to_date": "2026-02-01",
        "audience": "clientes",
    }

    response = client.post("/v1/release-notes", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "approved"
    assert "## Release v1.4.0" in body["release_notes"]

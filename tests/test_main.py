import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert len(response.json()) >= 0
    assert "status" in response.json().keys()
    assert response.json()["status"] == "ok"

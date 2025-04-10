import pytest
from fastapi.testclient import TestClient
from main import app, fake_db

client = TestClient(app)

def test_get_care_sessions():
    response = client.get("/care_sessions")
    assert response.status_code == 200
    assert len(response.json()) >= 0

def test_get_care_session_by_id():
    response = client.get("/care_sessions/1")
    assert response.status_code == 200
    assert type(response.json()) == dict
    assert response.json()["id"] == 1

def test_delete_care_session():
    count = len(fake_db["care_sessions"])

    response = client.delete("/care_sessions/1")
    assert response.status_code == 202
    assert response.json() == {"ok": True}
    assert len(fake_db["care_sessions"]) == count - 1

    count = len(fake_db["care_sessions"])
    response = client.delete("/care_sessions/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Care session not found"
    assert len(fake_db["care_sessions"]) == count



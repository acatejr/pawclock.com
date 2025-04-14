from fastapi.testclient import TestClient
from main import app
import pytest
from main import create_db_and_tables


@pytest.fixture(scope="session", autouse=True)
def prep_test_environ(request):
    create_db_and_tables()


def test_create_owner():
    client = TestClient(app)
    owner_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@email.com.invalid",
        "phone": "555-555-5555",
    }
    response = client.post("/owners/", json=owner_data)
    assert response.status_code == 201


def test_get_owners():
    client = TestClient(app)

    response = client.get("/owners")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 0


def test_get_owner():
    client = TestClient(app)

    owner_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@email.com.invalid",
        "phone": "555-555-5555",
    }
    response = client.post("/owners/", json=owner_data)
    assert response.status_code == 201

    owner_id = response.json()["id"]
    response = client.get(f"/owner/{owner_id}")
    assert response.status_code == 200
    assert response.json()["id"] == owner_id


def test_update_owner():
    client = TestClient(app)

    owner_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@email.com.invalid",
        "phone": "555-555-5555",
    }
    response = client.post("/owners/", json=owner_data)
    assert response.status_code == 201
    owner_id = response.json()["id"]

    updated_owner_data = {
        "first_name": "John Updated",
        "last_name": "Doe Updated",
        "email": "jdoe.updated@email.com.invalid",
        "phone": "555-555-5555",
    }
    response = client.patch(f"/owner/{owner_id}", json=updated_owner_data)
    assert response.status_code == 200
    assert response.json()["first_name"] == updated_owner_data["first_name"]


def test_delete_owner():
    client = TestClient(app)

    owner_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@email.com.invalid",
        "phone": "555-555-5555",
    }
    response = client.post("/owners/", json=owner_data)
    assert response.status_code == 201
    owner_id = response.json()["id"]

    response = client.delete(f"/owners/{owner_id}")
    assert response.status_code == 202
    assert response.json()["ok"] == True
    assert response.json()["id"] == owner_id
    assert response.json()["deleted"] == 1

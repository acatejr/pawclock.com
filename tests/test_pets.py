from fastapi.testclient import TestClient
from main import app
import pytest
from main import create_db_and_tables


@pytest.fixture(scope="session", autouse=True)
def prep_test_environ(request):
    create_db_and_tables()


def test_create_pet():
    client = TestClient(app)
    pet_data = {"name": "Fluffy"}
    response = client.post("/pets/", json=pet_data)

    assert response.status_code == 201
    assert response.json()["name"] == pet_data["name"]
    assert "id" in response.json().keys()


def test_delete_pet():
    client = TestClient(app)
    pet_data = {"name": "Rufus"}
    response = client.post("/pets/", json=pet_data)
    assert response.status_code == 201
    pet_id = response.json()["id"]
    assert pet_id is not None

    response = client.delete(f"/pets/{pet_id}")
    assert response.status_code == 202
    assert response.json()["ok"] == True
    assert response.json()["id"] == pet_id
    assert response.json()["deleted"] == 1


def test_get_pets():
    client = TestClient(app)
    response = client.get("/pets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 0


def test_get_pet():
    client = TestClient(app)

    pet_data = {"name": "David"}
    response = client.post("/pets/", json=pet_data)
    assert response.status_code == 201
    pet_id = response.json()["id"]

    response = client.get(f"/pet/{pet_id}")
    assert response.status_code == 200
    assert response.json()["id"] == pet_id


def test_update_pet():
    client = TestClient(app)
    pet_data = {"name": "Steve"}
    response = client.post("/pets/", json=pet_data)
    assert response.status_code == 201
    pet_id = response.json()["id"]

    updated_pet_data = {"name": "Steve Updated"}
    response = client.patch(f"/pets/{pet_id}", json=updated_pet_data)
    assert response.status_code == 200
    assert response.json()["name"] == updated_pet_data["name"]


# def test_delete_non_existent_pet():
#     pet_data = 9999
#     response = client.delete(f"/pets/{pet_data}")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "Pet not found"

# tests/test_users.py
from fastapi.testclient import TestClient
from main import app
from main import Pet, update_pet_in_db

client = TestClient(app)

def test_get_pet():
    pet_data = 1
    response = client.get(f"/pets/{pet_data}")
    assert response.status_code == 200
    assert response.json()["id"] == pet_data

def test_get_pets():
    response = client.get("/pets")
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_create_pet():
    pet_data = {"id": 0, "name": "Fluffy"}
    response = client.post("/pets/", json=pet_data)
    assert response.status_code == 201
    assert response.json()["name"] == pet_data["name"]

def test_delete_pet():
    pet_data = 1
    response = client.delete(f"/pets/{pet_data}")
    assert response.status_code == 202
    assert response.json()["ok"] == True

def test_delete_non_existent_pet():
    pet_data = 9999
    response = client.delete(f"/pets/{pet_data}")
    assert response.status_code == 404    
    assert response.json()["detail"] == "Pet not found"

def test_update_pet():
    pet_id = 9
    pet = {"id": pet_id, "name": "Steve"}
    response = client.put(f"/pets/{pet_id}", json=pet)
    assert response.status_code == 200
    assert response.json()["name"] == pet["name"]

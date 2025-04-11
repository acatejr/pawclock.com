# import pytest
# from fastapi.testclient import TestClient
# from main import Owner, app, fake_db

# client = TestClient(app)

# @pytest.fixture
# def reset_fake_db():
#     """
#     Fixture to reset the fake_db before each test.
#     """
#     original_owners = [
#         {"first_name": "John", "last_name": "Doe", "pets": [1]},
#         {"first_name": "Jane", "last_name": "Smith", "pets": [2]},
#         {"first_name": "Alice", "last_name": "Johnson", "pets": [3]},
#     ]
#     fake_db["owners"] = original_owners
#     yield
#     fake_db["owners"] = original_owners


# def test_get_owners(reset_fake_db):
#     response = client.get("/owners")
#     assert response.status_code == 200
#     assert len(response.json()) == 3
#     assert response.json()[0]["first_name"] == "John"


# def test_get_owner_by_id(reset_fake_db):
#     response = client.get("/owners/1")
#     assert response.status_code == 200
#     assert response.json()["first_name"] == "John"

#     response = client.get("/owners/999")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "Owner not found"


# def test_create_owner():
#     new_owner = {"first_name": "Bob", "last_name": "Brown", "pets": [4]}
#     response = client.post("/owners", json=new_owner)
#     print(response.json())
#     # assert response.status_code == 201
#     # assert response.json()["first_name"] == "Bob"
#     # assert len(fake_db["owners"]) == 4


# def test_update_owner(reset_fake_db):
#     updated_owner = {"id": 1, "first_name": "Johnathan", "last_name": "Doe", "pets": [1]}
#     response = client.put("/owners/1", json=updated_owner)
#     assert response.status_code == 200
#     assert response.json()["first_name"] == "Johnathan"

#     response = client.put("/owners/999", json=updated_owner)
#     assert response.status_code == 404
#     assert response.json()["detail"] == "Owner not found"


# def test_delete_owner(reset_fake_db):
#     response = client.delete("/owners/1")
#     assert response.status_code == 200
#     assert response.json()["ok"] is True
#     assert len(fake_db["owners"]) == 2

#     response = client.delete("/owners/999")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "Owner not found"

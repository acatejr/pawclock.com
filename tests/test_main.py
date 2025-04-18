import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlmodel import Session
from main import app
import database
import schema
import faker

client = TestClient(app)
fake = faker.Faker()

@pytest.fixture(name="owner_data")
def owner_data_fixture():

    data = {
        "id": 0,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.basic_phone_number(),
    }
    yield data

    # yield schema.Owner(
    #     id=0,
    #     first_name=fake.first_name(),
    #     last_name=fake.last_name(),
    #     email=fake.email(),
    #     phone=fake.basic_phone_number(),
    # )


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///pawclock_dev.db", echo=False)

    with Session(engine) as session:
        yield session


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert len(response.json()) >= 0
    assert "status" in response.json().keys()
    assert response.json()["status"] == "ok"


def test_create_pet():
    response = client.post(
        "/pets/",
        json={"id": 0, "name": "dog"},
    )

    assert response.status_code == 201
    assert response.json()["name"] == "dog"
    assert "id" in response.json().keys()
    assert response.json()["id"] > 0


def test_create_pet_invalid():
    response = client.post(
        "/pets/",
        json={"id": 0, "name": 0},
    )

    assert response.status_code == 422


def test_delete_pet(session: Session):
    pet_data = schema.PetCreate(
        id=0,
        name="dog",
    )

    pet = database.create_pet(
        session,
        pet_data,
    )

    response = client.delete(f"/pets/{pet.id}")
    assert response.status_code == 202
    assert response.json()["ok"] is True
    assert response.json()["deleted"] == 1


def test_get_pets(session: Session):
    response = client.get("/pets")
    assert response.status_code == 200
    assert len(response.json()) >= 0


def test_get_pet(session: Session):
    pet_data = schema.PetCreate(
        id=0,
        name="dog",
    )

    pet = database.create_pet(
        session,
        pet_data,
    )

    response = client.get(f"/pets/{pet.id}")
    assert response.status_code == 200
    assert response.json()["name"] == "dog"
    assert response.json()["id"] == pet.id


def test_update_pet(session: Session):

    pet_data = schema.PetCreate(
        id=0,
        name="dork",
    )

    pet = database.create_pet(
        session,
        pet_data,
    )

    pet_name = fake.name() + " updated"
    pet_data = schema.Pet(
        id=pet.id,
        name=pet_name
    )
    response = client.patch(
        f"/pets/{pet.id}",
        json=pet_data.model_dump(),
    )

    assert response.status_code == 200
    assert response.json()["name"] == pet_name
    assert response.json()["id"] == pet.id


def test_create_owner(session: Session, owner_data):

    resp = client.post(
        "/owners/",
        json=owner_data,
    )

    assert resp.status_code == 201
    assert resp.json()["first_name"] == owner_data.first_name
    assert resp.json()["last_name"] == owner_data.last_name
    assert resp.json()["email"] == owner_data.email
    assert resp.json()["phone"] == owner_data.phone
    assert resp.json()["id"] > 0

def test_delete_owner(session: Session):
    owner_data = schema.OwnerCreate(
        id=0,
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        phone=fake.basic_phone_number(),
    )
    obj = database.create_owner(session, owner_data)
    assert obj is not None
    resp = client.delete(f"/owners/{obj.id}")
    assert resp.status_code == 202

    assert resp.json()["ok"] is True
    assert resp.json()["deleted"] == 1

def test_get_owner(session: Session, owner_data):
    obj = database.create_owner(session, owner_data)
    assert obj is not None

    resp = client.get(f"/owner/{obj.id}")
    assert resp.status_code == 200
    assert resp.json()["first_name"] == owner_data.first_name
    assert resp.json()["last_name"] == owner_data.last_name
    assert resp.json()["email"] == owner_data.email
    assert resp.json()["phone"] == owner_data.phone
    assert resp.json()["id"] == obj.id


def test_get_owners(session: Session):
    resp = client.get("/owners")
    assert resp.status_code == 200
    assert len(resp.json()) >= 0


def test_update_owner(session: Session, owner_data):

    target_owner_data = schema.OwnerCreate(
        id=0,
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        phone=fake.basic_phone_number(),
    )

    obj = database.create_owner(session, target_owner_data)
    assert obj is not None
    assert obj.id is not None
    owner_id = obj.id

    updated_owner_data = schema.Owner(
        id=owner_id,
        first_name=fake.first_name() + " updated",
        last_name=fake.last_name() + " updated",
        email=fake.email() + " updated",
        phone=fake.basic_phone_number() + " updated",
    )

    response = client.patch(
        f"/owners/{owner_id}",
        json=updated_owner_data.model_dump(),
    )

    assert response.status_code == 200
    assert response.json()["first_name"] == updated_owner_data.first_name
    assert response.json()["last_name"] == updated_owner_data.last_name
    assert response.json()["email"] == updated_owner_data.email
    assert response.json()["phone"] == updated_owner_data.phone
    assert response.json()["id"] == owner_id

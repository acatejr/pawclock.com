import pytest
import database
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import datetime


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///pawclock_dev.db", echo=False)
    # Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session


@pytest.fixture(autouse=True)
def owner_data():
    # This fixture will run before each test
    # You can set up any necessary data or state here
    # For example, you could create a test owner in the database

    # yield to allow the test to run

    # This code will run after each test
    # You can clean up any data or state here
    owner_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@email.com.invalid",
        "phone": "1234567890",
    }
    yield owner_data


@pytest.fixture(autouse=True)
def pet_data():
    # This fixture will run before each test
    # You can set up any necessary data or state here
    # For example, you could create a test pet in the database

    # yield to allow the test to run

    # This code will run after each test
    # You can clean up any data or state here
    pet_data = {"id": 0, "name": "Fluffy"}
    yield pet_data

def test_update_owner(session: Session, owner_data):
    obj = database.create_owner(session, owner_data)
    assert obj is not None
    assert obj.first_name == owner_data["first_name"]
    assert obj.last_name == owner_data["last_name"]
    assert obj.email == owner_data["email"]
    assert obj.phone == owner_data["phone"]
    owner_id = obj.id

    updated_owner_data = {"first_name": "Jane"}

    obj = database.update_owner(session, owner_id, updated_owner_data)
    assert obj is not None
    assert obj.first_name == updated_owner_data["first_name"]
    assert obj.id == owner_id


def test_get_owners(session: Session):
    resp = database.get_owners(session)
    assert resp is not None
    assert len(resp) >= 0


def test_get_owner(session: Session, owner_data):
    obj = database.create_owner(session, owner_data)
    assert obj is not None
    owner_id = obj.id

    resp = database.get_owner(session, owner_id)
    assert resp is not None
    assert resp.first_name == owner_data["first_name"]
    assert resp.last_name == owner_data["last_name"]
    assert resp.email == owner_data["email"]
    assert resp.phone == owner_data["phone"]
    assert resp.id == owner_id


def test_create_owner(session: Session, owner_data):
    obj = database.create_owner(session, owner_data)
    assert obj is not None
    assert obj.first_name == owner_data["first_name"]
    assert obj.last_name == owner_data["last_name"]
    assert obj.email == owner_data["email"]
    assert obj.phone == owner_data["phone"]
    assert obj.id is not None


def test_delete_owner(session: Session, owner_data):
    obj = database.create_owner(session, owner_data)
    assert obj is not None
    assert obj.id is not None
    owner_id = obj.id

    resp = database.delete_owner(session, owner_id)
    assert resp is not None
    assert resp == 1


def test_create_pet(session: Session, pet_data):
    obj = database.create_pet(session, pet_data)

    assert obj is not None
    assert obj.name == pet_data["name"]
    assert obj.id is not None
    assert obj.id > 0


def test_delete_pet(session, pet_data):

    obj = database.create_pet(session, pet_data)
    resp = database.delete_pet(session, obj.id)
    assert resp is not None
    assert resp == 1


def test_delete_invalid_pet(session):
    resp = database.delete_pet(session, 9999)
    assert resp is 0


def test_get_pet(session, pet_data):

    obj = database.create_pet(session, pet_data)
    resp = database.get_pet(session, obj.id)
    assert resp is not None
    assert resp.name == pet_data["name"]
    assert resp.id == obj.id


def test_get_pets(session):
    resp = database.get_pets(session)

    assert resp is not None
    assert len(resp) >= 0


def test_update_pet(session, pet_data):

    obj = database.create_pet(session, pet_data)
    assert obj is not None
    assert obj.name == pet_data["name"]
    pet_id = obj.id

    updated_pet_data = {"name": "Fido"}

    obj = database.update_pet(session, obj.id, updated_pet_data)
    assert obj is not None
    assert obj.name == updated_pet_data["name"]
    assert obj.id == pet_id

def test_create_care_session(session, pet_data, owner_data):
    obj = database.create_pet(session, pet_data)
    assert obj is not None
    assert obj.name == pet_data["name"]
    pet_id = obj.id

    obj = database.create_owner(session, owner_data)
    assert obj is not None
    assert obj.first_name == owner_data["first_name"]
    assert obj.last_name == owner_data["last_name"]
    assert obj.email == owner_data["email"]
    assert obj.phone == owner_data["phone"]
    owner_id = obj.id

    now = datetime.datetime.now()
    care_session_data = {
        "pet_id": pet_id,
        "owner_id": owner_id,
        "start_date": now,
    }

    resp = database.create_care_session(session, care_session_data)
    assert resp is not None
    assert resp.pet_id == pet_id
    assert resp.owner_id == owner_id
    assert resp.start_date == now
    assert resp.end_date is None
    assert resp.id is not None


# @pytest.fixture(name="setup_db")
# def setup_db(session: Session):
#     # Create the database tables
#     database.create_db_and_tables()

#     # Add test data if needed
#     # session.add(models.Pet(name="Test Pet"))
#     # session.commit()

#     yield session

#     # Clean up the database after tests
#     session.query(database.models.Pet).delete()
#     session.query(database.models.Owner).delete()
#     session.commit()

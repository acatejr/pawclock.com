import pytest
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker, Session
from models import Pet, Owner, Base
from sqlalchemy.exc import IntegrityError

ECHO_SQL = True

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine('sqlite:///pawclock_test.db', echo=ECHO_SQL)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        # tables = [Pet.__tablename__, Owner.__tablename__]
        # for table in tables:
        #     session.execute(text(f"DELETE FROM {table}"))
        #     session.commit()
        yield session


def test_create_valid_owner(session: Session):
    owner = Owner(
        first_name="John",
        last_name="Doe",
        email="jdoe@email.com.invalid",
        phone="1234567890"
    )

    session.add(owner)
    session.flush()
    session.refresh(owner)

    assert owner.first_name == "John"
    assert owner.last_name == "Doe"
    assert owner.email == "jdoe@email.com.invalid"
    assert owner.id is not None


# def test_create_invalid_owners(session: Session):
#     owner_no_first_name = Owner(
#         first_name=None,
#         last_name="Doe",
#         email="jdoe@email.com.invalid",
#         phone="1234567890"
#     )

#     session.add(owner_no_first_name)

#     owner_no_last_name = Owner(
#         first_name="Harry",
#         last_name=None,
#         email="jdoe@email.com.invalid",
#         phone="1234567890"
#     )

#     session.add(owner_no_last_name)

#     owner_no_phone = Owner(
#         first_name="Harry",
#         last_name="Doe",
#         email="jdoe@email.com.invalid",
#         phone=None
#     )

#     session.add(owner_no_phone)

#     with pytest.raises(IntegrityError):
#         session.commit()


# def test_create_valid_pet(session: Session):
#     pet = Pet(
#         name="Fluffy"
#     )

#     session.add(pet)
#     session.flush()
#     session.refresh(pet)

#     assert pet.name == "Fluffy"
#     assert pet.id is not None


# def test_create_invalid_pet(session: Session):
#     pet_no_name = Pet(
#         name=None
#     )

#     session.add(pet_no_name)

#     with pytest.raises(IntegrityError):
#         session.commit()


# def test_create_owners_with_pets(session: Session):
#     pets = [
#         Pet(name="Fluffy"),
#         Pet(name="Fido"),
#         Pet(name="Whiskers"),
#         Pet(name="Spot"),
#     ]

#     owner = Owner(
#         first_name="John",
#         last_name="Doe",
#         phone="1234567890",
#         pets=pets
#     )

#     session.add(owner)
#     session.flush()
#     session.refresh(owner)

#     assert owner.first_name == "John"
#     assert owner.last_name == "Doe"
#     assert owner.phone == "1234567890"
#     assert len(owner.pets) == 4

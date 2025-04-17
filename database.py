from sqlalchemy.orm import Session
import models


def create_care_session(session: Session, care_session_data: dict):
    care_session = models.CareSession(
        start_date=care_session_data["start_date"],
        # end_date=care_session_data["end_date"],
        pet_id=care_session_data["pet_id"],
        owner_id=care_session_data["owner_id"],
    )

    session.add(care_session)
    session.commit()
    session.refresh(care_session)

    return care_session


def update_owner(session: Session, owner_id: int, owner_data: dict):
    owner = session.query(models.Owner).filter(models.Owner.id == owner_id).first()

    if not owner:
        return None

    for key, value in owner_data.items():
        setattr(owner, key, value)

    session.commit()
    session.refresh(owner)

    return owner


def get_owners(session: Session):
    owners = session.query(models.Owner).all()
    return owners


def get_owner(session: Session, owner_id: int):
    owner = session.query(models.Owner).filter(models.Owner.id == owner_id).first()
    return owner


def delete_owner(session: Session, owner_id: int):
    obj = session.query(models.Owner).filter(models.Owner.id == owner_id).delete()
    session.commit()

    return obj


def create_owner(session: Session, owner_data: dict):
    owner = models.Owner(
        first_name=owner_data["first_name"],
        last_name=owner_data["last_name"],
        email=owner_data["email"],
        phone=owner_data["phone"],
    )

    session.add(owner)
    session.commit()
    session.refresh(owner)

    return owner


def get_pets(session: Session):
    pets = session.query(models.Pet).all()
    return pets


def get_pet(session: Session, pet_id: int):
    pet = session.query(models.Pet).filter(models.Pet.id == pet_id).first()
    return pet


def create_pet(session: Session, pet_data: dict):
    pet = models.Pet(
        name=pet_data["name"],
    )

    session.add(pet)
    session.commit()
    session.refresh(pet)

    return pet


def delete_pet(session: Session, pet_id: int):
    obj = session.query(models.Pet).filter(models.Pet.id == pet_id).delete()
    session.commit()

    return obj


def update_pet(session: Session, pet_id: int, pet_data: dict):
    pet = session.query(models.Pet).filter(models.Pet.id == pet_id).first()

    if not pet:
        return None

    for key, value in pet_data.items():
        setattr(pet, key, value)

    session.commit()
    session.refresh(pet)

    return pet

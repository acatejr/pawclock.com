# from typing import Union

from fastapi import FastAPI, Depends, HTTPException, Query
from contextlib import asynccontextmanager
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import models
import schema
import database

# from models import Pet, PetCreate, PetPublic
# from models import Owner, OwnerCreate, OwnerPublic
# from sqlmodel import Session, create_engine, SQLModel, select

ECHO_SQL = False


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="PawClock API", description="PawClock API", version="0.1.0", lifespan=lifespan
)

engine = create_engine("sqlite:///pawclock_dev.db", echo=ECHO_SQL)

# Base.metadata.create_all(engine)
# sqlite_file_name = "pawclock_dev.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
# connect_args = {"check_same_thread": False}
# engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    models.Base.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


@app.get("/health")
async def health():
    now = datetime.now()
    return {"status": "ok", "msg": now}


@app.post("/pets/", response_model=schema.Pet, status_code=201)
async def create_pet(pet: schema.PetCreate, session: Session = Depends(get_session)):
    new_pet = models.Pet(
        name=pet.name,
    )

    session.add(new_pet)
    session.commit()
    session.refresh(new_pet)

    return new_pet


@app.delete("/pets/{pet_id}", status_code=202)
async def delete_pet(*, session: Session = Depends(get_session), pet_id: int):
    result = database.delete_pet(session, pet_id)

    # pet = session.get(schema.Pet, pet_id)
    # print(pet)

    # if not pet:
    #     raise HTTPException(status_code=404, detail="Pet not found")

    # session.delete(pet)
    # session.commit()

    return {"ok": True, "id": pet_id, "deleted": 1}


# @app.post("/owners/", response_model=OwnerPublic, status_code=201)
# async def create_owner(*, session: Session = Depends(get_session), owner: OwnerCreate):
#     db_owner = Owner.model_validate(owner)
#     session.add(db_owner)
#     session.commit()
#     session.refresh(db_owner)
#     return db_owner


# @app.get("/owners", response_model=list[OwnerPublic])
# async def get_owners(
#     *,
#     session: Session = Depends(get_session),
#     offset: int = 0,
#     limit: int = Query(default=10, le=100),
# ):
#     owners = session.exec(select(Owner).offset(offset).limit(limit)).all()

#     return owners


# @app.get("/owner/{owner_id}", response_model=OwnerPublic)
# async def get_owner(*, session: Session = Depends(get_session), owner_id: int):
#     owner = session.get(Owner, owner_id)

#     if not owner:
#         raise HTTPException(status_code=404, detail="Owner not found")

#     return owner


# @app.patch("/owner/{owner_id}", response_model=OwnerPublic)
# async def update_owner(
#     *, session: Session = Depends(get_session), owner_id: int, owner: OwnerCreate
# ):
#     db_owner = session.get(Owner, owner_id)

#     if not db_owner:
#         raise HTTPException(status_code=404, detail="Owner not found")

#     db_owner_data = owner.model_dump(exclude_unset=True)
#     for key, value in db_owner_data.items():
#         setattr(db_owner, key, value)

#     session.add(db_owner)
#     session.commit()
#     session.refresh(db_owner)

#     return db_owner


# @app.delete("/owners/{owner_id}", status_code=202)
# async def delete_owner(*, session: Session = Depends(get_session), owner_id: int):
#     owner = session.get(Owner, owner_id)

#     if not owner:
#         raise HTTPException(status_code=404, detail="Owner not found")

#     session.delete(owner)
#     session.commit()

#     return {"ok": True, "id": owner_id, "deleted": 1}


# @app.get("/pet/{pet_id}", response_model=PetPublic)
# async def get_pet(*, session: Session = Depends(get_session), pet_id: int):
#     pet = session.get(Pet, pet_id)

#     if not pet:
#         raise HTTPException(status_code=404, detail="Pet not found")

#     return pet


# @app.get("/pets", response_model=list[PetPublic])
# async def get_pets(
#     *,
#     session: Session = Depends(get_session),
#     offset: int = 0,
#     limit: int = Query(default=10, le=100),
# ):
#     pets = session.exec(select(Pet).offset(offset).limit(limit)).all()
#     return pets


# @app.delete("/pets/{pet_id}", status_code=202)
# async def delete_pet(*, session: Session = Depends(get_session), pet_id: int):
#     pet = session.get(Pet, pet_id)

#     if not pet:
#         raise HTTPException(status_code=404, detail="Pet not found")

#     session.delete(pet)
#     session.commit()

#     return {"ok": True, "id": pet_id, "deleted": 1}


# @app.patch("/pets/{pet_id}", response_model=PetPublic)
# async def update_pet(
#     *, session: Session = Depends(get_session), pet_id: int, pet: PetCreate
# ):
#     db_pet = session.get(Pet, pet_id)

#     if not db_pet:
#         raise HTTPException(status_code=404, detail="Pet not found")

#     db_pet_data = pet.model_dump(exclude_unset=True)
#     for key, value in db_pet_data.items():
#         setattr(db_pet, key, value)

#     session.add(db_pet)
#     session.commit()
#     session.refresh(db_pet)

#     return db_pet

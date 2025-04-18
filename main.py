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
        id=0,
        name=pet.name,
    )

    new_pet = database.create_pet(session, new_pet)
    session.add(new_pet)
    session.commit()
    session.refresh(new_pet)

    return new_pet


@app.delete("/pets/{pet_id}", status_code=202)
async def delete_pet(*, session: Session = Depends(get_session), pet_id: int):
    result = database.delete_pet(session, pet_id)

    return {"ok": True, "id": pet_id, "deleted": 1}


@app.get("/pets", response_model=list[schema.Pet])
async def get_pets(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=10, le=100),
):
    pets = database.get_pets(session)
    if not pets:
        raise HTTPException(status_code=404, detail="Pets not found")
    return pets


@app.get("/pets/{pet_id}", response_model=schema.Pet)
async def get_pet(*, session: Session = Depends(get_session), pet_id: int):
    pet = database.get_pet(session, pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    return pet


@app.patch("/pets/{pet_id}", response_model=schema.Pet)
async def update_pet(
    *, session: Session = Depends(get_session), pet_id: int, pet: schema.PetCreate
):
    updated_pet = database.update_pet(session, pet_id, pet.model_dump(exclude_unset=True))
    if not updated_pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    return updated_pet


@app.post("/owners/", response_model=schema.Owner, status_code=201)
async def create_owner(
    owner: schema.OwnerCreate, session: Session = Depends(get_session)
):
    new_owner = models.Owner(
        id=0,
        first_name=owner.first_name,
        last_name=owner.last_name,
        email=owner.email,
        phone=owner.phone,
    )
    new_owner = database.create_owner(session, new_owner)

    return new_owner


@app.delete("/owners/{owner_id}", status_code=202)
async def delete_owner(*, session: Session = Depends(get_session), owner_id: int):
    result = database.delete_owner(session, owner_id)
    if result == 1:
        return {"ok": True, "id": owner_id, "deleted": 1}
    else:
        raise HTTPException(status_code=404, detail="Owner not found")


@app.get("/owner/{owner_id}", response_model=schema.Owner)
async def get_owner(*, session: Session = Depends(get_session), owner_id: int):
    owner = database.get_owner(session, owner_id)  # session.get(Owner, owner_id)

    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")

    return owner


@app.get("/owners", response_model=list[schema.Owner])
async def get_owners(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=10, le=100),
):

    owners = database.get_owners(session)

    if not owners:
        raise HTTPException(status_code=404, detail="Owners not found")

    return owners


@app.patch("/owners/{owner_id}", response_model=schema.Owner)
async def update_owner(
    *, session: Session = Depends(get_session), owner_id: int, owner: schema.OwnerCreate
):

    updated_owner = database.update_owner(session, owner_id, owner.model_dump(exclude_unset=True))
    if not updated_owner:
        raise HTTPException(status_code=404, detail="Owner not found")

    return updated_owner

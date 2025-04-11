# from typing import Union

from fastapi import FastAPI, Depends, HTTPException, Query
from datetime import datetime
from models import Pet, PetCreate, PetPublic
from sqlmodel import Session, create_engine, SQLModel, select
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="PawClock API", description="PawClock API", version="0.1.0", lifespan=lifespan
)

sqlite_file_name = "pawclock.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


@app.get("/health")
async def health():
    now = datetime.now()
    return {"status": "ok", "msg": now}


@app.get("/pet/{pet_id}", response_model=PetPublic)
def get_pet(*, session: Session = Depends(get_session), pet_id: int):
    pet = session.get(Pet, pet_id)

    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    return pet


@app.get("/pets", response_model=list[PetPublic])
def get_pets(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=10, le=100),
):
    pets = session.exec(select(Pet).offset(offset).limit(limit)).all()
    return pets


@app.post("/pets/", response_model=PetPublic, status_code=201)
def create_pet(*, session: Session = Depends(get_session), pet: PetCreate):
    db_pet = Pet.model_validate(pet)
    session.add(db_pet)
    session.commit()
    session.refresh(db_pet)
    return db_pet


@app.delete("/pets/{pet_id}", status_code=202)
async def delete_pet(*, session: Session = Depends(get_session), pet_id: int):
    pet = session.get(Pet, pet_id)

    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    session.delete(pet)
    session.commit()

    return {"ok": True, "id": pet_id, "deleted": 1}


@app.patch("/pets/{pet_id}", response_model=PetPublic)
def update_pet(*, session: Session = Depends(get_session), pet_id: int, pet: PetCreate):
    db_pet = session.get(Pet, pet_id)

    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    db_pet_data = pet.model_dump(exclude_unset=True)
    for key, value in db_pet_data.items():
        setattr(db_pet, key, value)

    session.add(db_pet)
    session.commit()
    session.refresh(db_pet)

    return db_pet

    # pet_data = pet.model_dump(exclude_unset=True)
    # for key, value in pet_data.items():
    #     setattr(pet, key, value)
    # session


if __name__ == "__main__":
    create_db_and_tables()


# @app.get("/owners")
# async def get_owners() -> list[Owner]:
#     owners = fake_db["owners"]
#     return owners

# @app.get("/owners/{owner_id}")
# async def get_owner(owner_id: int) -> Owner:

#     for owner in fake_db["owners"]:
#         if owner["id"] == owner_id:
#             return owner

#     raise HTTPException(status_code=404, detail="Owner not found")

# @app.post("/owners", response_class=JSONResponse, status_code=201)
# async def create_owner(owner: Owner):
#     print(owner)
#     new_owner = {} #create_new_owner(owner)
#     return new_owner

# # @app.put("/owners/{owner_id}", response_model=Owner)
# # async def update_owner(owner_id: int, owner: Owner):
# #     updated_owner = await update_owner_in_db(owner_id, owner)
# #     if not updated_owner:
# #         raise HTTPException(status_code=404, detail="Owner not found")
# #     return updated_owner

# # @app.delete("/owners/{owner_id}", response_model=dict)
# # async def delete_owner(owner_id: int):
# #     result = await delete_owner_from_db(owner_id)
# #     if not result:
# #         raise HTTPException(status_code=404, detail="Owner not found")
# #     return {"ok": result}

# @app.get("/care_sessions", response_model=list[CareSession], status_code=200)
# async def get_care_sessions():
#     """
#     Get a list of all care sessions.
#     """
#     return fake_db["care_sessions"]

# @app.get("/care_sessions/{session_id}", response_model=CareSession, status_code=200)
# async def get_care_session(session_id: int):
#     """
#     Get a specific care session by ID.
#     """
#     for session in fake_db["care_sessions"]:
#         if session["id"] == session_id:
#             return session

#     raise HTTPException(status_code=404, detail="Care session not found")

# @app.delete("/care_sessions/{session_id}", response_class=JSONResponse, status_code=202)
# async def delete_care_session(session_id: int):
#     """
#     Delete a care session by ID.
#     """

#     for session in fake_db["care_sessions"]:
#         if session["id"] == session_id:
#             fake_db["care_sessions"].remove(session)
#             return {"ok": True}

#     raise HTTPException(status_code=404, detail="Care session not found")


# async def get_pet_by_id_from_db(pet_id) -> Pet:
#     # Simulate a database query
#     for pet in fake_db["pets"]:
#         if pet["id"] == pet_id:
#             return pet
#     return None

# async def update_pet_in_db(pet_id: int, pet: Pet):
#     # Simulate a database update operation
#     for i, p in enumerate(fake_db["pets"]):
#         if pet_id == p["id"]:
#             found_pet_idx = i
#             fake_db["pets"][i] = pet
#             return fake_db["pets"][i]

#     return None

# async def delete_pet_from_db(pet_id: int) -> bool:
#     # Simulate a database delete operation
#     for pet in fake_db["pets"]:
#         if pet["id"] == pet_id:
#             fake_db["pets"].remove(pet)
#             return True
#     return False

# async def get_pets_from_db() -> list[Pet]:
#     # Simulate a database call
#     return fake_db["pets"]

# async def create_new_owner(owner: Owner) -> Owner:
#     # Simulate a database insert operation
#     new_owner = {"id": len(fake_db["owners"]) + 1, **owner.dict()}
#     fake_db["owners"].append(new_owner)
#     return new_owner

# """
# =========================================
# """
# # @app.get("/owners", response_model=list[Owner])
# # async def get_owners():
# #     """
# #     Get a list of all owners.
# #     """
# #     return fake_db["owners"]


# # @app.get("/owners/{owner_id}", response_model=Owner)
# # async def get_owner(owner_id: int):
# #     """
# #     Get a specific owner by ID.
# #     """
# #     owner = await get_owner_by_id_from_db(owner_id)
# #     if not owner:
# #         raise HTTPException(status_code=404, detail="Owner not found")
# #     return owner


# # @app.post("/owners", response_model=Owner, status_code=201)
# # async def create_owner(owner: Owner):
# #     """
# #     Create a new owner.
# #     """
# #     new_owner = {"id": len(fake_db["owners"]) + 1, **owner.dict()}
# #     fake_db["owners"].append(new_owner)
# #     return new_owner


# # @app.put("/owners/{owner_id}", response_model=Owner)
# # async def update_owner(owner_id: int, owner: Owner):
# #     """
# #     Update an existing owner by ID.
# #     """
# #     updated_owner = await update_owner_in_db(owner_id, owner)
# #     if not updated_owner:
# #         raise HTTPException(status_code=404, detail="Owner not found")
# #     return updated_owner


# # @app.delete("/owners/{owner_id}", response_model=dict)
# # async def delete_owner(owner_id: int):
# #     """
# #     Delete an owner by ID.
# #     """
# #     result = await delete_owner_from_db(owner_id)
# #     if not result:
# #         raise HTTPException(status_code=404, detail="Owner not found")
# #     return {"ok": result}


# # # Helper functions for Owner operations
# # async def get_owner_by_id_from_db(owner_id: int) -> dict:
# #     """
# #     Simulate a database query to get an owner by ID.
# #     """
# #     for owner in fake_db["owners"]:
# #         if owner["id"] == owner_id:
# #             return owner
# #     return None


# # async def update_owner_in_db(owner_id: int, owner: Owner) -> dict:
# #     """
# #     Simulate a database update operation for an owner.
# #     """
# #     for i, o in enumerate(fake_db["owners"]):
# #         if o["id"] == owner_id:
# #             fake_db["owners"][i] = {"id": owner_id, **owner.dict()}
# #             return fake_db["owners"][i]
# #     return None


# # async def delete_owner_from_db(owner_id: int) -> bool:
# #     """
# #     Simulate a database delete operation for an owner.
# #     """
# #     for owner in fake_db["owners"]:
# #         if owner["id"] == owner_id:
# #             fake_db["owners"].remove(owner)
# #             return True
# #     return False

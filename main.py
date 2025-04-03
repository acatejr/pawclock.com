from typing import Union
from fastapi import FastAPI, HTTPException
from datetime import datetime
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(
    title="PawClock API", 
    description="PawClock API", 
    version="0.1.0"
)

fake_db = {
    "pets": [
        {"id": 1, "name": "Buddy"},
        {"id": 2, "name": "Mittens"},
        {"id": 3, "name": "Goldie"},
        {"id": 4, "name": "Charlie"},
        {"id": 5, "name": "Max"},
        {"id": 6, "name": "Bella"},
        {"id": 7, "name": "Lucy"},
        {"id": 8, "name": "Daisy"},
        {"id": 9, "name": "Luna"},
        {"id": 10, "name": "Rocky"},
    ],
    "owners": [
        {"id": 1, "first_name": "John", "last_name": "Doe", "pets": [1]},
        {"id": 2, "first_name": "Jane", "last_name": "Smith", "pets": [2]},
        {"id": 3, "first_name": "Alice", "last_name": "Johnson", "pets": [3]},
        {"id": 4, "first_name": "Bob", "last_name": "Brown", "pets": [4]},
        {"id": 5, "first_name": "Charlie", "last_name": "Davis", "pets": [5]},
        {"id": 6, "first_name": "Dave", "last_name": "Wilson", "pets": [6]},
        {"id": 7, "first_name": "Eve", "last_name": "Taylor", "pets": [7]},
        {"id": 8, "first_name": "Frank", "last_name": "Anderson", "pets": [8]},
        {"id": 9, "first_name": "Grace", "last_name": "Thomas", "pets": [9]},
        {"id": 10, "first_name": "Greg", "last_name": "Martinez", "pets": [10]},
    ],
}

class Pet(BaseModel):
    id: int
    name: str
    # species: str
    # age: int
    # weight: float

    def __str__(self):
        return f"Pet(id={self.id}, name={self.name})"

class Owner(BaseModel):
    id: int
    first_name: str
    last_name: str
    pets: list[int]  # List of pet IDs

    def __str__(self):
        return f"Owner(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, pets={self.pets})"
    
@app.get("/health")
async def health():
    now = datetime.now()
    return {"msg": now}


@app.get("/pets")
async def get_pets() -> list[Pet]:
    pets = await get_pets_from_db()
    return pets

@app.post("/pets/", response_model=Pet, status_code=201)
async def create_pet(pet: Pet):
    pet = {"id": 1, "name": pet.name}
    return pet

@app.get("/pets/{pet_id}", response_class=JSONResponse, status_code=200)
async def get_pet(pet_id: int):

    pet = await get_pet_by_id_from_db(pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@app.delete("/pets/{pet_id}", response_class=JSONResponse, status_code=202)
async def delete_pet(pet_id: int):
    result = await delete_pet_from_db(pet_id)
    
    if not result:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    return {"ok": result}

@app.put("/pets/{pet_id}", response_class=JSONResponse, status_code=200)
async def update_pet(pet_id: int, Pet: Pet):
    """
    if new pet response code is 200
    if update pet response code is 201
    if not found response code is 404
    """
    result = await update_pet_in_db(pet_id, Pet)
    if not result:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    return result

async def get_pet_by_id_from_db(pet_id) -> Pet:
    # Simulate a database query
    for pet in fake_db["pets"]:
        if pet["id"] == pet_id:
            return pet
    return None

async def update_pet_in_db(pet_id: int, pet: Pet):
    # Simulate a database update operation
    for i, p in enumerate(fake_db["pets"]):
        if pet_id == p["id"]:
            found_pet_idx = i
            fake_db["pets"][i] = pet
            return fake_db["pets"][i]
    
    return None
    
async def delete_pet_from_db(pet_id: int) -> bool:
    # Simulate a database delete operation
    for pet in fake_db["pets"]:
        if pet["id"] == pet_id:
            fake_db["pets"].remove(pet)
            return True
    return False

async def get_pets_from_db() -> list[Pet]:
    # Simulate a database call
    return fake_db["pets"]

"""
=========================================
"""
# @app.get("/owners", response_model=list[Owner])
# async def get_owners():
#     """
#     Get a list of all owners.
#     """
#     return fake_db["owners"]


# @app.get("/owners/{owner_id}", response_model=Owner)
# async def get_owner(owner_id: int):
#     """
#     Get a specific owner by ID.
#     """
#     owner = await get_owner_by_id_from_db(owner_id)
#     if not owner:
#         raise HTTPException(status_code=404, detail="Owner not found")
#     return owner


# @app.post("/owners", response_model=Owner, status_code=201)
# async def create_owner(owner: Owner):
#     """
#     Create a new owner.
#     """
#     new_owner = {"id": len(fake_db["owners"]) + 1, **owner.dict()}
#     fake_db["owners"].append(new_owner)
#     return new_owner


# @app.put("/owners/{owner_id}", response_model=Owner)
# async def update_owner(owner_id: int, owner: Owner):
#     """
#     Update an existing owner by ID.
#     """
#     updated_owner = await update_owner_in_db(owner_id, owner)
#     if not updated_owner:
#         raise HTTPException(status_code=404, detail="Owner not found")
#     return updated_owner


# @app.delete("/owners/{owner_id}", response_model=dict)
# async def delete_owner(owner_id: int):
#     """
#     Delete an owner by ID.
#     """
#     result = await delete_owner_from_db(owner_id)
#     if not result:
#         raise HTTPException(status_code=404, detail="Owner not found")
#     return {"ok": result}


# # Helper functions for Owner operations
# async def get_owner_by_id_from_db(owner_id: int) -> dict:
#     """
#     Simulate a database query to get an owner by ID.
#     """
#     for owner in fake_db["owners"]:
#         if owner["id"] == owner_id:
#             return owner
#     return None


# async def update_owner_in_db(owner_id: int, owner: Owner) -> dict:
#     """
#     Simulate a database update operation for an owner.
#     """
#     for i, o in enumerate(fake_db["owners"]):
#         if o["id"] == owner_id:
#             fake_db["owners"][i] = {"id": owner_id, **owner.dict()}
#             return fake_db["owners"][i]
#     return None


# async def delete_owner_from_db(owner_id: int) -> bool:
#     """
#     Simulate a database delete operation for an owner.
#     """
#     for owner in fake_db["owners"]:
#         if owner["id"] == owner_id:
#             fake_db["owners"].remove(owner)
#             return True
#     return False

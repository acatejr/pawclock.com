from typing import Optional
from sqlmodel import SQLModel, Field


class PetBase(SQLModel):
    name: str


class Pet(PetBase, table=True):
    __tablename__ = "pets"
    id: Optional[int] = Field(default=None, primary_key=True)


class PetCreate(PetBase):
    pass


class PetPublic(PetBase):
    id: int


class OwnerBase(SQLModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    # pets: list[PetPublic] = []


class Owner(OwnerBase, table=True):
    __tablename__ = "owners"
    id: Optional[int] = Field(default=None, primary_key=True)
    # pets: list[PetPublic] = []


class OwnerCreate(OwnerBase):
    pass


class OwnerPublic(OwnerBase):
    id: int
    # pets: list[PetPublic] = []

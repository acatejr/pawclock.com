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

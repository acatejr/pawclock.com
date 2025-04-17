from pydantic import BaseModel


class PetBase(BaseModel):
    id: int
    name: str
    # owners: list[int] = []
    # care_sessions: list[int] = []


class PetCreate(PetBase):
    pass


class Pet(PetBase):
    id: int
    # name: str
    # owners: list[int] = []
    # care_sessions: list[int] = []

    # class Config:
    # orm_mode = True
    # from_attributes = True

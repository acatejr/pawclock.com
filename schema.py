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


class OwnerBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str


class OwnerCreate(OwnerBase):
    pass


class Owner(OwnerBase):
    id: int

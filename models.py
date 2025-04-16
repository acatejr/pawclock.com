# from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=False)
    pets = relationship("Pet", secondary="owners_pets", back_populates="owners")


class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    owners = relationship("Owner", secondary="owners_pets", back_populates="pets")


class OwnerPet(Base):
    __tablename__ = 'owners_pets'
    owner_id = Column(Integer, ForeignKey('owners.id'), primary_key=True)
    pet_id = Column(Integer, ForeignKey('pets.id'), primary_key=True)


# Create a SQLite database in memory for demonstration purposes
# engine = create_engine('sqlite:///:memory:')

# from typing import Optional
# from sqlmodel import SQLModel, Field


# class PetBase(SQLModel):
#     name: str


# class Pet(PetBase, table=True):
#     __tablename__ = "pets"
#     id: Optional[int] = Field(default=None, primary_key=True)


# class PetCreate(PetBase):
#     pass


# class PetPublic(PetBase):
#     id: int


# class OwnerBase(SQLModel):
#     first_name: str
#     last_name: str
#     email: str
#     phone: str
#     # pets: list[PetPublic] = []


# class Owner(OwnerBase, table=True):
#     __tablename__ = "owners"
#     id: Optional[int] = Field(default=None, primary_key=True)
#     # pets: list[PetPublic] = []


# class OwnerCreate(OwnerBase):
#     pass


# class OwnerPublic(OwnerBase):
#     id: int
#     # pets: list[PetPublic] = []

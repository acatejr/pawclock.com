# from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy import ForeignKey, String, Integer, text, func
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=False)
    pets = relationship("Pet", secondary="owners_pets", back_populates="owners")

    def __repr__(self):
        return f"<Owner(id={self.id}, first_name={self.first_name}, last_name={self.last_name})>"


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    owners = relationship("Owner", secondary="owners_pets", back_populates="pets")

    def __repr__(self):
        return f"<Pet(id={self.id}, name={self.name})>"


class OwnerPet(Base):
    __tablename__ = "owners_pets"
    owner_id = Column(Integer, ForeignKey("owners.id"), primary_key=True)
    pet_id = Column(Integer, ForeignKey("pets.id"), primary_key=True)


class CareSession(Base):
    __tablename__ = "care_sessions"

    id = Column(Integer, primary_key=True)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    owner_id = Column(Integer, ForeignKey("owners.id"), nullable=False)
    start_date = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    end_date = Column(DateTime(timezone=True))


# Create a SQLite database in memory for demonstration purposes
# engine = create_engine('sqlite:///:memory:')

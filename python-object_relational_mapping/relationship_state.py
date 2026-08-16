#!/usr/bin/python3
"""Defines the State class linked to the MySQL table states,
with a relationship to City."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Represents a state in the MySQL database.

    Attributes:
        id: The primary key, an auto-generated unique integer.
        name: The name of the state.
        cities: Relationship to all City objects linked to this state.
            Deleting a State cascades and deletes its linked City rows.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", backref="state", cascade="all, delete-orphan"
    )

#!/usr/bin/python3
"""Defines the City class linked to the MySQL table cities."""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Represents a city in the MySQL database.

    Attributes:
        id: The primary key, an auto-generated unique integer.
        name: The name of the city.
        state_id: Foreign key referencing the id of the linked State.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

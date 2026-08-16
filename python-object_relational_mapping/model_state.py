#!/usr/bin/python3
"""Defines the State class linked to the MySQL table states."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state in the MySQL database.

    Attributes:
        id: The primary key, an auto-generated unique integer.
        name: The name of the state.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

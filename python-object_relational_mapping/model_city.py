#!/usr/bin/python3
"""First state model"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City table class

    Args:
        Base (type): Declarative base for a class
    """
    __tablename__ = "cities"

    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  unique=True,
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey("states.id"),
                      nullable=False
                      )

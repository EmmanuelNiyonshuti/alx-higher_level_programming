#!/usr/bin/python3
"""This Script contains the class definition of a City.
"""
from relationship_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class City (Base):
    """City table that inherits from declarative base"""
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False,  unique=True,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')

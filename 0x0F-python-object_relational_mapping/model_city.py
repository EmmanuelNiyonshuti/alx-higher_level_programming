#!/usr/bin/python3
"""
"""
from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class City (Base):
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('State')
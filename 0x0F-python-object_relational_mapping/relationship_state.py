#!/usr/bin/python3
"""Contains a class definition of a State and an instance Base.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State (Base):
    """state class that inherits from base"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False,
                autoincrement=True, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state', cascade='delete')

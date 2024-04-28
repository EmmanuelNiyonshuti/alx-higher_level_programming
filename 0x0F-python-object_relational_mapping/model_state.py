#!/usr/bin/python3
"""Contains a class definition of a State and an instance Base.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

Base = declarative_base()
url = f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()


class State (Base):
    """state class that inherits from base"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False,
                autoincrement=True, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)

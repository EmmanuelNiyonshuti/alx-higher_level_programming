#!/usr/bin/python3
""" This script prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_state_connect import engine, session

if __name__ == "__main__":

    first_state = session.query(State).first()
    if not first_state:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    session.close()

#!/usr/bin/python3
""" This script prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    url = f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).first()
    if not first_state:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    session.close()

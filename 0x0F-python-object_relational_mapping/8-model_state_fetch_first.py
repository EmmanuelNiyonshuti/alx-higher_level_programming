#!/usr/bin/python3
""" This script prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    if not State:
        print()
    else:
        query = session.query(State).first()
        print(f"{query.id}: {query.name}")
    session.close()
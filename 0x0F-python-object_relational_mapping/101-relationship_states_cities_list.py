#!/usr/bin/python3

"""This script lists all State objects and corresponding City objects
Contained in the database.
"""
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":

    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f"mysql://{user_name}:{passwd}@localhost/{db}")

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(asc(State.id)).all()
    for state in query:
        print(f"{state.name}: {state.id}")
        for city in state.cities:
            print(f"   {city.id}: {city.name}")

    session.close()

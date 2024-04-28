#!/usr/bin/python3
"""This script that lists all City objects from the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":

    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    url = f"mysql://{user_name}:{passwd}@localhost/{db}"
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).all()
    for state in query:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()

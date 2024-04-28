#!/usr/bin/python3
"""This script creates the State "California"
With the City "San Francisco" from the database hbtn_0e_100_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":

    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f"mysql://{user_name}:{passwd}@localhost/{db}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = State(name="California")
    city_name = City(name="San Francisco", state=state_name)

    session.add_all([state_name, city_name])
    session.commit()
    session.close()

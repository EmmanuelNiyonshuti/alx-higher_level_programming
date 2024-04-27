#!/usr/bin/python3
"""
This script deletes all States objects
with a name containing the letter a from the database  hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State).filter(State.name.like('%a%')).all()

    for state in q:
        session.delete(state)
    session.commit()
    session.close()
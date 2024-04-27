#!/usr/bin/python3
"""This script lists all State objects ordered by their ids in asc
    from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """Create a sessionmaker with an engine"""
    Session = sessionmaker(bind=engine)
    """Create a session instance"""
    session = Session()

    query = session.query(State).order_by(asc(State.id))
    result = query.all()
    for state in result:
        print(f"{state.id}: {state.name}")
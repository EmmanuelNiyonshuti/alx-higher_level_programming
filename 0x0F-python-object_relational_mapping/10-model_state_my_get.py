#!/usr/bin/python3
"""
This script prints the state object with the name passed as argument
from the database hbtn_0e_6_usa.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, bindparam
import sys
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine("mysql://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    querry = session.query(State).filter(State.name == bindparam('state_name'))
    result = querry.params(state_name=sys.argv[4]).all()
    if not result:
        print("Not Found")
    else:
        for state in result:
            print(state.id)
    session.close()
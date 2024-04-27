#!/usr/bin/python3
"""
This script prints the state object with the name passed as argument
from the database hbtn_0e_6_usa.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    querry = session.query(State).filter(State.name == sys.argv[4])
    result = querry.first()
    if not result:
        print("Not Found")
    else:
        print(result.id)

    session.close()

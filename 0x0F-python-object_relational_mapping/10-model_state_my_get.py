#!/usr/bin/python3
"""
This script prints the state object with the name passed as argument
from the database hbtn_0e_6_usa.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import text
import sys
from model_state import Base, State

if __name__ == "__main__":
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine("mysql://{}:{}@localhost/{}".format(
        user_name, passwd, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    querry = session.query(State).filter(State.name == text(':name'))

    result = querry.params(name=state_name).all()
    if not result:
        print("Not Found")
    else:
        [print(f"{state.id}") for state in result]

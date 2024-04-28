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

    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql://{}:{}@localhost/{}".format(
        user_name, passwd, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = sys.argv[4]
    querry = session.query(State).filter(State.name == state_name)
    result = querry.first()
    if not result:
        print("Not Found")
    else:
        print(result.id)
    session.close()
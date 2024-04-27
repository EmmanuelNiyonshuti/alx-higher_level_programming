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

    engine = create_engine("mysql://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    querry = session.query(State).filter(State.name == text(':name'))
    result = querry.params(name=sys.argv[4]).all()
    if not result:
        print("Not Found")
    else:
        [print(f"{state.id}") for state in result]

    #using bindparam class
    # param_name = bindparam('param_name', value=sys.argv[4])

    # querry = session.query(State).filter(State.name == param_name).order_by(State.id)
    # result = querry.all()
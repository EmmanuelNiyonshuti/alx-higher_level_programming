#!/usr/bin/python3
"""
This script prints all City object from the database hbtn_0e_14_usa.
"""
from model_city import City
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    engine = create_engine("mysql://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(City).order_by(asc(City.id)).all()

    for city in q:
        print(f"{city.state.name}: ({city.id}) {city.name}")
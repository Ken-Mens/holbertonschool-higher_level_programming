#!/usr/bin/python3
"""print all Cities from database"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
import MySQLdb

username = argv[1]
password = argv[2]
database = argv[3]

if __name__ == '__main__':

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                        (argv[1], argv[2], argv[3], pool_pre_ping=True))

    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    sesh = Session()
    ok = sesh.query(State, City)

    for state, city in ok.filter(City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

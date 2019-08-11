#!/usr/bin/python3
# 11-filter_cities.py: takes in name of a state as an argument and list cities
""" filter cities by State
"""
if __name__ == "__main__":

    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]

    from model_state import Base, State
    from sqlalchemy import create_engine
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                        (argv[1], argv[2], argv[3], pool_pre_ping=True))

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=eng)
    sesh = Session()

    louisiana = State(name="Louisiana")
    sesh.add(louisiana)
    sesh.commit()
    print(louisiana.id)

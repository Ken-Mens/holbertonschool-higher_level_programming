#!/usr/bin/python3
# 5-filter_cities.py: takes in name of a state as an argument and list cities
""" filter cities by State
"""
if __name__ == "__main__":

    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]
    statename = argv[4]

    from model_state import Base, State
    from sqlalchemy import create_engine
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                        (argv[1], argv[2], argv[3], pool_pre_ping=True))

    from sqlalchemy.orm import sessionmaker
    sesh = sessionmaker(bind=eng)

    Base.metadata.create_all(eng)
    ok = sesh().query(State).filter(State.name == argv[4]).all()
    if ok:
        for state in ok:
            if state.name == argv[4]:
                print("{}".format(state.id))
    else:
        print("Not found")
    sesh().close()

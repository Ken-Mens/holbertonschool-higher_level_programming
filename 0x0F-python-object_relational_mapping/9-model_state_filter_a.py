#!/usr/bin/python3
# 8-model_state_fetch_all.py: lists all States from a database

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

    Session = sessionmaker(bind=eng)
    sesh = Session()

    for state in sesh.query(State) \
        .order_by(State.id):
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))

    sesh.close()

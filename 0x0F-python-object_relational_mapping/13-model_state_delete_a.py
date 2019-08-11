#!/usr/bin/python3
# 13-model_state_delete_a.py: deletes all State objects with 'a'
""" Delete states
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
    Base.metadata.create_all(eng)

    for stat in sesh.query(State).order_by(State.id):
        if 'a' in stat.name:
            sesh.delete(stat)
    sesh.commit()
    sesh.close()

#!/usr/bin/python3
# 12-model_state_update_id_2.py: script that changes the name of a State
""" filter cities by State
"""
if __name__ == "__main__":

    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]

    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                        (argv[1], argv[2], argv[3], pool_pre_ping=True))

    Session = sessionmaker(bind=eng)
    sesh = Session()
    Base.metadata.create_all(eng)

    NM = sesh.query(State).filter_by(id=2).first()
    NM.name = "New Mexico"
    sesh.commit()

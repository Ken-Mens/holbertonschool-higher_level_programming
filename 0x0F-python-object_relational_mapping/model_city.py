#!/usr/bin/python3
# model_city.py: contains class definition of a City

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """ City Class """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)

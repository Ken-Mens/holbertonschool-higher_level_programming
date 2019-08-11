#!/usr/bin/python3
# model_city.py: contains class definition of a City

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ City Class """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey(State.id))

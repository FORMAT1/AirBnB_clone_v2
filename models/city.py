#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Foreignkey, String

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
     __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    stat_id = Column(String(60), nullable=False, foreignkey=("states.id"))

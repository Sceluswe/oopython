#!/usr/bin/env python3

""" Mapping of class """

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Human(Base):
    """
    Class mapped to the database farm.sqlite.
    """
    __tablename__ = "humans"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    occupation = Column(String)
    age = Column(Integer)

    def __init__(self, str_name, str_occupation, int_age):
        """ init method """
        self.name = str_name
        self.occupation = str_occupation
        self.age = int_age

    def __str__(self):
        return "Name: {n}, Occupation: {o}, Age: {a}".format(n=self.name, o=self.occupation, a=self.age)

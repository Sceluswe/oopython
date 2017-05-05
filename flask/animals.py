#!/usr/bin/env python3

""" Mapping of class """

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Animal(Base):
    """
    Class mapped to the database farm.sqlite.
    """
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    species = Column(String)
    name = Column(String)
    nr_of_legs = Column(Integer)

    def __init__(self, str_species, str_name, int_nrOfLegs):
        """ init method """
        self.species = str_species
        self.name = str_name
        self.nr_of_legs = int_nrOfLegs

    def __str__(self):
        return "Species: {s}, Name: {n}, Legs: {l}".format(s=self.species, n=self.name, l=self.nr_of_legs)

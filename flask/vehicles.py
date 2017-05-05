#!/usr/bin/env python3

""" Mapping of class """

from sqlalchemy import Column, Float, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Vehicle(Base):
    """
    Class mapped to the database farm.sqlite.
    """
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)
    vehicle_type = Column(String)
    price = Column(Float)

    def __init__(self, str_vehicleType, float_price):
        """ init method """
        self.vehicle_type = str_vehicleType
        self.price = float_price


    def __str__(self):
        return "Model: {m}, Price: {p}".format(m=self.vehicle_type, p=self.price)

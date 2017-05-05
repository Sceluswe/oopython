#!/usr/bin/env python3

"""
A module for the person class.
"""

class Person:
    """
    A class containing information about a person.
    """

    def __init__(self, firstname, lastname, age, adress):
        """
        Constructor.
        """
        self.str_firstname = firstname
        self.str_lastname = lastname
        self.int_age = age
        self.str_adress = adress

    def getName(self):
        """
        Returns just the name of the Person.
        """
        return self.str_firstname + " " + self.str_lastname

    def getAge(self):
        """
        Returns just the name of the Person.
        """
        return self.int_age

    def getAdress(self):
        """
        Returns just the name of the Person.
        """
        return self.str_adress

    def __str__(self):
        """
        Str for Person.
        """
        return self.str_firstname + " " + self.str_lastname + ", age: " + self.int_age + ", " + self.str_adress

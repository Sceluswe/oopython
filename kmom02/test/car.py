"""
A module for a car.
"""

class Car():
    """
    A class with basic car functionality.
    """
    wheels = 4
    carCount = 0

    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.equipment = list()

        Car.carCount += 1


    def presentCar(self):
        """Print car"""
        print("Model: {m}, Price: {p}".format(m=self.model, p=self.price))

    @staticmethod
    def calculatePriceReduction(aPrice):
        """Calculate price"""
        return int(aPrice * 0.66)

    def reducePrice(self):
        """Reduce price"""
        self.price = self.calculatePriceReduction(self.price)
        return "Priset för {c} är nu {p}".format(c=self.model, p=self.price)

    def addEquipment(self, newEquipment):
        """Add any sort of equipment object"""
        self.equipment.append(newEquipment)

    def printEquipment(self):
        """ Print all equipment objects"""
        for eq in self.equipment:
            print("* " + eq)

    def __add__(self, other):
        """Operator add"""
        return self.price + other.price

    def __iadd__(self, other):
        """Operator add"""
        self.price += other.price
        return self

"""
A Dog class.
"""

class Dog:
    """
    A dog.
    """

    def __init__(self, str_name, str_size, str_race, int_numberOfDays):
        """
        Constructor.
        """
        self.str_name = str_name
        self.str_size = str_size
        self.str_race = str_race
        self.int_numberOfDays = int_numberOfDays

    def info(self):
        """
        Returns the info of dog as a string.
        """
        str_result = "name: " + self.str_name + ", size: " + self.str_size
        return str_result + ", race: " + self.str_race + ", nrOfDays: " + str(self.int_numberOfDays)

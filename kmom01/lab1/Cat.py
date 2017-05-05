"""
A Cat class.
"""

import Animal

class Cat(Animal.Animal):
    """
    A class of a Cat.
    """
    int_nrOfPaws = 4

    def __init__(self, str_eyeColor, str_name):
        super(Cat, self).__init__(str_eyeColor, str_name)
        self.int_livesLeft = -1
        self._bool_evil = True

    def description(self):
        """
        Returns a string with cat description.
        """
        str_desc = "My cats name is {name}, has {color} eyes and {livesLeft} lives left to live."

        return str_desc.format(name=self.str_name, color=self.str_eyeColor, livesLeft=self.int_livesLeft)

    def isEvil(self):
        """
        Returns if the cat is evil or not.
        """
        return self._bool_evil

    def speak(self):
        """
        The sound a cat makes.
        """
        return "Meow"

"""
A Dog class.
"""

import Animal
import Cat

class Dog(Animal.Animal):
    """
    A class of a Dog.
    """
    def __init__(self, str_eyeColor, str_name):
        super(Dog, self).__init__(str_eyeColor, str_name)
        self.int_livesLeft = 1

    @staticmethod
    def interact(obj):
        """
        Dog interacts with objects.
        """
        str_result = "Lick!"

        if isinstance(obj, Cat.Cat):
            str_result = "Chase!"

        return str_result


    def description(self):
        """
        Returns a string with Dogs description.
        """
        str_desc = "My dogs name is {name}, has {color} eyes and {livesLeft} lives left to live."

        return str_desc.format(name=self.str_name, color=self.str_eyeColor, livesLeft=self.int_livesLeft)

    def speak(self):
        """
        The sound a dog makes.
        """
        return "Voff"

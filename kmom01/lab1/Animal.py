"""
A Animal parent class for more specialised animals.
"""

class Animal():
    """
    The Animal class.
    """

    def __init__(self, str_eyeColor, str_name):
        self.str_name = str_name
        self.str_eyeColor = str_eyeColor

    def speak(self):
        """
        Function that returns an animals common sound.
        """
        raise NotImplementedError("Subclasses should implement this!")

    def speakTwice(self):
        """
        Makes the animal speak twice.
        """
        return self.speak() + " " + self.speak()

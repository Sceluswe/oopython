"""
A module for the card class.
"""

class Card:
    """
    Containts card specific data.
    """

    # Static variables keeping track of all names and suits.
    # index 0 is none so that the value of the cards is the index.
    names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

    def __init__(self, value, suit):
        """
        Constructor.
        """
        self.value = value
        self.suit = suit

    def __str__(self):
        """
        Returns an information string about the class.
        """
        return self.names[self.value] + " of " + self.suits[self.suit]

    def __eq__(self, other):
        """
        Equlaity operator: card == card
        """
        result = False

        if self.value == other.value and self.suit == other.suit:
            result = True

        return result

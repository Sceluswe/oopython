"""
A module for the hand class.
"""

import deck

class Hand(deck.Deck):
    """
    A Hand containing a set of cards.
    """
    def __init__(self):
        """
        Constructor.
        """
        super().__init__()
        self.cards = list()

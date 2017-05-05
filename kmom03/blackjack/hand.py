"""
A module for the hand class.
"""

import deck
# might be redundant:parent has import card
import card

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

    def sumOfHand(self):
        """
        Returns the sum of hand.
        """
        sumOfHand = 0
        for mycard in self.cards:
            sumOfHand += mycard.value

        return sumOfHand

    def showHand(self):
        """
        Shows all cards in your hand.
        """
        for mycard in self.cards:
            # Show card.
            print(mycard)

    def getCard(self, index):
        """
        Show one card in the hand.
        """
        return self.cards[index]

    def getCardSuit(self, index):
        """
        Show one cards suit in the hand.
        """
        return card.Card.suits[self.cards[index].suit]

    def resetDeck(self):
        """
        Overload parent function. Reset deck = make it empty.
        """
        self.cards = list()

    def __eq__(self, other):
        """
        Equlaity operator: card == card
        """
        result = False

        for i, eachcard in enumerate(self.cards):
            result = eachcard == other.cards[i]

        return result

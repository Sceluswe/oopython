"""
Contains the deck class.
"""

import random
import card

class Deck:
    """
    A deck containing cards.
    """

    def __init__(self):
        """
        Constructor.
        """
        self.cards = list()
        self.resetDeck()

    def __str__(self):
        """
        Returns an information string about Deck.
        """
        str_result = ""

        for i, eachCard in enumerate(self.cards):
            str_result += "card" + str(i + 1) + ": " + eachCard.__str__() + "\n"

        return str_result

    def shuffle(self):
        """
        Shuffles the deck in a random order.
        """
        random.shuffle(self.cards)

    def takeCard(self, obj_cardDeck):
        """
        Removes a random card from the deck argument.
        """
        card_picked = random.choice(obj_cardDeck.cards)
        # Delete card from deck.
        del obj_cardDeck.cards[card_picked.value]
        # Add the card to self.
        self.cards.append(card_picked)

    def addCard(self, obj_card):
        """
        Takes a card and adds it to the deck.
        """
        self.cards.append(obj_card)

    def playCard(self, index):
        """
        Plays a card from your hand and removes it.
        """
        # Save card in local variable.
        card_result = self.cards[index]
        # Delete the card from the list.
        del self.cards[index]
        # "Play" card.
        print("Played: " + card_result.info())

    def resetDeck(self):
        """
        Resets deck by creating a 52 card deck, unshuffled.
        """
        for suit in range(len(card.Card.suits)):
            for i in range(1, len(card.Card.names)):
                self.addCard(card.Card(i, suit))

#!/usr/bin/env python3

"""
Main applikation window to test the code.
"""

import unittest
import deck
import hand as handimport
import card

class Testcase(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    card1 = card.Card(1, 0)
    deckOfCards = deck.Deck()
    deckOfCards.shuffle()

    hand = handimport.Hand()

    # Test Card class.
    def test_deck_attribute(self):
        """ Returns True if instances are the same """
        self.assertEqual(self.card1.value, 1)
        self.assertEqual(self.card1.suit, 0)

    def test_str_method(self):
        """ Returns true if success """
        self.assertEqual(self.card1.__str__(), "Ace of Spades")

    # Test Hand class.
    def test_hand_card_list(self):
        """ Returns true if cards is list and empty """
        newHand = handimport.Hand()
        self.assertIsInstance(newHand.cards, list)
        self.assertEqual(newHand.cards, [])

    def test_parent_of_hand(self):
        """ Returns true if hand parent is deck. """
        self.assertIsInstance(self.hand, deck.Deck)

    def test_hand_takeCard_method(self):
        """ Returns true if cards were added """
        newHand = handimport.Hand()
        newHand.takeCard(self.deckOfCards)
        newHand.takeCard(self.deckOfCards)
        newHand.takeCard(self.deckOfCards)
        newHand.takeCard(self.deckOfCards)
        newHand.takeCard(self.deckOfCards)

        # Test if the size is 4
        self.assertEqual(len(newHand.cards), 5)

        for item in newHand.cards:
            # Makes sure we only have cards.
            self.assertIsInstance(item, card.Card)
            # Makes sure each card is of valid suit.
            self.assertIn(card.Card.suits[item.suit], card.Card.suits)
            # Make sure each card has a valid value, remove None from names.
            list_withoutNone = card.Card.names[1:]
            self.assertIn(card.Card.names[item.value], list_withoutNone)

    # Test Deck class.
    def test_deck_resetMethod(self):
        """ Returns true if all attributes are correct """
        # Reset to default if recent changes have happened.
        newDeck = deck.Deck()

        # Test default length,
        self.assertEqual(len(newDeck.cards), 52)

        # Try taking 3 cards.
        self.hand.takeCard(newDeck)
        self.hand.takeCard(newDeck)
        self.hand.takeCard(newDeck)

        # Test length again.
        self.assertEqual(len(newDeck.cards), 49)

        newDeck.resetDeck()
        # Test default length,
        self.assertEqual(len(newDeck.cards), 52)

    def test_deck_shuffleMethod(self):
        """ Returns true if the deck was shuffled """
        shuffledDeck = deck.Deck()
        unshuffledDeck = deck.Deck()

        self.assertEqual(len(shuffledDeck.cards), len(unshuffledDeck.cards))

        # Make sure both new Decks produced the same sorted decks.
        for i in range(len(unshuffledDeck.cards)):
            self.assertEqual(unshuffledDeck.cards[i].value, shuffledDeck.cards[i].value)
            self.assertEqual(unshuffledDeck.cards[i].suit, shuffledDeck.cards[i].suit)


        shuffledDeck.shuffle()

        self.assertNotEqual(unshuffledDeck, shuffledDeck)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3

"""
Main applikation window to test the code.
"""

import deck
import hand

deckOfCards = deck.Deck()
deckOfCards.shuffle()

hand = hand.Hand()

hand.takeCard(deckOfCards)
hand.takeCard(deckOfCards)
hand.takeCard(deckOfCards)
hand.takeCard(deckOfCards)
hand.takeCard(deckOfCards)



print(deckOfCards)
hand.showHand()

print("\nPlaying this card:")
deckOfCards.playCard(5)

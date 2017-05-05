#!/usr/bin/env python3

"""
Main applikation window for the blackjack game.
"""
import deck
import hand

# Create X number of Hands (one for each player) based on previous input.
playingPlayers = list()
# Create 1 deck.
ourDeck = deck.Deck()
# Shuffle deck.
ourDeck.shuffle()

for i in range(3):
    playingPlayers.append(hand.Hand())
    # Give each player 2 starting cards.
    playingPlayers[i].takeCard(ourDeck)
    playingPlayers[i].takeCard(ourDeck)

# Save players that have stayed:
stayedPlayers = list()

# ---------------- Gameloop ----------------
# Create a loop that goes from player to player.
for i, player in enumerate(playingPlayers):
    playing = True

    # Ask if the player wants to play.
    playerChoice = input("Do you want to stay? yes/no y/n\n-->")

    if "yes" in playerChoice or "y" in playerChoice:
        playing = False
        stayedPlayers.append(playingPlayers[i])
        del playingPlayers[i]

print(playingPlayers)
print(stayedPlayers)

# deleting a player while inside a for loop seems to keep things going smoothly.

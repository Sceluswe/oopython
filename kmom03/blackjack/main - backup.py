#!/usr/bin/env python3

"""
Main applikation window for the blackjack game.
"""

# make it so that the players can play another round, so that the game doesn't
# end! And allow players to press q in order to quit whenever they want to.

# Add the ability for a SINGLE player to leave the table.

import deck
import hand



# anti-redundancy function
def dealerSaysHand(hand_obj, str_more=None):
    """
    The dealer calls out the cards of the player and possibly more.
    """
    print("Dealer: You have:")
    hand_obj.showHand()
    print("Sum: " + str(hand_obj.sumOfHand()))
    if str_more != None:
        print(str_more)
    print("\n")



# Ask for the amount of players
int_nrOfPlayers = int(input("How many players?\n-->"))

if int(int_nrOfPlayers) > 0:
    # Create 1 deck.
    ourDeck = deck.Deck()

    # Shuffle deck.
    ourDeck.shuffle()

    # Create 1 dealer.
    dealer = hand.Hand()

    # Give the dealer ONE card.
    dealer.takeCard(ourDeck)

    # Create X number of Hands (one for each player) based on previous input.
    playingPlayers = list()
    for i in range(0, int_nrOfPlayers):
        # Create player/Hand.
        playingPlayers.append(hand.Hand())

        # Give each player 2 starting cards.
        playingPlayers[i].takeCard(ourDeck)
        playingPlayers[i].takeCard(ourDeck)

    # Save players that have stayed:
    stayingPlayers = list()



# ---------------- Gameloop ----------------
    # Create a loop that goes from player to player.

    print("PLAYERS:")
    print(playingPlayers)
    print("LENGTH OF LIST: " + str(int_nrOfPlayers))
    print(playingPlayers[0])
    print(playingPlayers[1])
    # For each player:
    counter = 0
    while counter < int_nrOfPlayers:
        print(counter)
        player = playingPlayers[counter]

        # Get the values of the players first two cards.
        card1 = player.getCard(0)
        card2 = player.getCard(1)
        card1Suit = player.getCardSuit(0)
        card2Suit = player.getCardSuit(1)

        # Check if the player has blackjack, otherwise let him play.
        if "Ace" in card1Suit or "Ace" in card2Suit and card1.value == 10 or card2.value == 10:
            # Print players hand.
            player.showHand()

            # Dealer tells player he has blackjack.
            dealerSaysHand(player, "Player" + str(counter + 1) + "you've got blackjack!")

            # save player in staying.
            stayingPlayers.append(playingPlayers[counter])

        else:
            playing = True

            # Let each player play until he has won or lost or decided to stay.
            while playing:
                print("\n\n\n// ------------------------")
                # Check the players score.
                # If he's got 21, it's next players turn and current player stays automatically.
                if player.sumOfHand() == 21:
                    playing = False

                    # Dealer tells player his score.
                    dealerSaysHand(player, "Player" + str(counter + 1) + " you got 21! You're maxed, good luck!")

                    # save player in staying.
                    stayingPlayers.append(playingPlayers[counter])

                # If he has more than 21 he has lost, end the game for him.
                elif player.sumOfHand() > 21:
                    playing = False

                    # Print that player has lost and is out.
                    dealerSaysHand(player, "Player" + str(counter + 1) + " exceeded 21, you're out! You have lost.")

                else:
                    # Ask if the player wants to play.
                    dealerSaysHand(player)
                    playerChoice = input("Player" + str(counter + 1) + " do you want to stay? yes/no y/n\n-->")

                    # If player wants to stay:
                    if "yes" in playerChoice or "y" in playerChoice:
                        playing = False

                        # save player in staying.
                        stayingPlayers.append(playingPlayers[counter])

                    # If player wants to play:
                    elif "no" in playerChoice or "n" in playerChoice:
                        # Give the player a card.
                        newCard = playingPlayers[counter].takeCard(ourDeck)

                        # Dealer tells player his new card.
                        dealerSaysHand(player, "Player" + str(counter + 1) + ", your new card: " + str(newCard.value))

                        # If he hasn't lost: Ask the him what he wants to do:
                # Loop starts over until player stays or loses.
        # Proceed to next player.
        counter += 1
        print("Player" + str(counter) + " done.")

    # When all players are done, the dealer plays like this:
    # When the dealer has won he stays, even if he has 18.
    # The dealer plays until he has won or lost. He doesn't stay if that makes him lose.

    # If the house wins, print that.
    # Otherwise print the stayingPlayer with the highest value, the winner.

"""
Contains the Blackjack class.
"""

import deck
import player

class Blackjack:
    """
    The game Blackjack.
    """
    def __init__(self, int_nrOfPlayers):
        """
        Constructor.
        """
        # Set number of players.
        self.int_nrOfPlayers = int_nrOfPlayers

        # Create 1 deck.
        self.gameDeck = deck.Deck()
        # Shuffle deck.
        self.gameDeck.shuffle()

        # Create X number of Hands (one for each player) based on previous input.
        self.list_playingPlayers = list()
        for i in range(0, int_nrOfPlayers):
            # Create player/Hand.
            self.list_playingPlayers.append(player.Player("Player" + str(i + 1)))

            # Give each player 2 starting cards.
            self.list_playingPlayers[i].takeCard(self.gameDeck)
            self.list_playingPlayers[i].takeCard(self.gameDeck)

        # List for players that are done playing/have stayed.
        self.list_stayingPlayers = list()

        # Create 1 dealer.
        self.dealer = player.Player("Dealer")


    # anti-redundancy function
    def dealerSaysHand(self, player_obj, str_more=None):
        """
        The dealer calls out the cards of the player and possibly more.
        """
        print(player_obj.str_playername + " has:")
        player_obj.showHand()
        print("Sum: " + str(player_obj.sumOfHand()))
        if str_more != None:
            print(str_more)
        print("\n")


    # play(player, "Player" + str(counter + 1))
    def play(self, player_obj):
        """
        Give a player a card
        """
        newCard = player_obj.takeCard(self.gameDeck)

        # Dealer tells player his new card.
        self.dealerSaysHand(player_obj, player_obj.str_playername + ", gets new card: " + str(newCard))


    def remove(self, player_obj):
        """
        Remove player from playing.
        """
        for i, eachplayer in enumerate(self.list_playingPlayers):
            if eachplayer == player_obj:
                del self.list_playingPlayers[i]


    # stay(player, "Player" + str(counter + 1))
    def stay(self, player_obj):
        """
        Move a player to the stayed list.
        """
        # save player in staying.
        self.list_stayingPlayers.append(player_obj)

        # remove player from playing.
        self.remove(player_obj)

        # Dealer proclaims who stayed.
        self.dealerSaysHand(player_obj, player_obj.str_playername + " stays.")


    def allowedToPlay(self, player_obj):
        """
        Check if the player can play= hasn't lost and doesn't have blackjack.
        And is in the correct list.
        """
        result = False

        if player_obj.sumOfHand() < 21:
            for eachplayer in self.list_playingPlayers:
                if player_obj == eachplayer:
                    result = True

        elif player_obj.sumOfHand() > 21 or player_obj.sumOfHand() == 21:
            result = False

        return result


    def won(self, player_obj):
        """
        Check if the player has won.
        """
        result = False

        if player_obj.sumOfHand() == 21:
            result = True

        return result


    def hasBlackjack(self, player_obj):
        """
        Check if player has blackjack.
        """
        result = False
        # Check if the player has blackjack.
        # Get the values of the players first two cards.
        card1 = player_obj.getCard(0)
        card2 = player_obj.getCard(1)
        card1Suit = player_obj.getCardSuit(0)
        card2Suit = player_obj.getCardSuit(1)

        if "Ace" in card1Suit and card2.value == 10 or "Ace" in card2Suit and card1.value == 10:
            result = True

        return result


    def lost(self, player_obj):
        """
        Check if the sum of players hand exceeds the limit.
        """
        result = False

        if player_obj.sumOfHand() > 21:
            result = True

        elif player_obj.sumOfHand() < 21:
            result = False

        return result

    def announceWinner(self):
        """
        Announce the highest scoring player as winner, announce price money.
        """
        highest = 0
        # Check who has the highest score.
        for eachplayer in self.list_stayingPlayers:
            if eachplayer.sumOfHand() > highest:
                highest = eachplayer.sumOfHand()
                winner = eachplayer

        # Announce the winner and the amount of money the winner won.
        print("The winner is: " + winner.str_playername + ", with a score of: " + str(winner.sumOfHand()))
        print("Earning: " + str(winner.highestBid) + " from players.")

        if(winner.str_playername != "Dealer"):
            print("Earning: " + str(winner.int_bid * 6) + " * 6 from dealer.")
        else:
            print("The house always wins.")

    def playDealer(self):
        """
        Make the dealers final moves.
        """
        # Find highest player number.
        highplayer = 0
        for eachplayer in self.list_stayingPlayers:
            if eachplayer.sumOfHand() > highplayer:
                highplayer = eachplayer.sumOfHand()

        # If dealer is lower.
        if self.dealer.sumOfHand() < 21 and self.dealer.sumOfHand() < highplayer:
            # get a new card.
            self.play(self.dealer)

        elif self.dealer.sumOfHand() > 21:
            # If dealer is higher than 21, dealer has lost.
            print("Dealer lost with:" + str(self.dealer.sumOfHand()))

        # If dealer is the highest.
        else:
            # Stay and move dealer to player list.
            self.stay(self.dealer)


    def gameloop(self):
        """
        The games gameloop, call this function to start the game.
        """
        # Give the dealer ONE card.
        self.play(self.dealer)

        # Let players play if there are playing players.
        while self.list_playingPlayers != list():
            # create shorthand
            player_obj = self.list_playingPlayers[0]

            # If player has not lost or won, play:
            if self.allowedToPlay(player_obj):
                # Display dealers card.
                self.dealerSaysHand(self.dealer)

                print("// -------------------------------")
                print("YOUR TURN: " + player_obj.str_playername + "\n")

                # Ask if the player wants to play.
                self.dealerSaysHand(player_obj)
                print(player_obj.str_playername + " bid: ")
                print(str(player_obj.int_bid) + " / " + str(player_obj.highestBid))

                print("// -------------------------------")
                print("bid [number] - Place a bet.")
                print("play - Ask the dealer for a new card.")
                print("stay - stay with your current cards.")
                print("quit - to EXIT the entire game session.")

                # Get player input.
                playerChoice = input(player_obj.str_playername + " -->")

                # If player wants to play:
                if playerChoice == "play" or playerChoice == "p":
                    # If player has not bet enough money he can't play.
                    if player_obj.highestBid == 0 or player_obj.int_bid >= player_obj.highestBid:
                        self.play(player_obj)
                    else:
                        print("OBS: You must bet at least: " + str(player_obj.highestBid))

                # If player wants to stay:
                elif playerChoice == "stay" or playerChoice == "s":
                    self.stay(player_obj)

                elif "bid" in playerChoice:
                    list_temp = playerChoice.split(" ")

                    if list_temp[1].isnumeric():
                        player_obj.placeBet(int(list_temp[1]))
                    else:
                        print("bid must be followed by a number.")

                elif playerChoice == "quit"  or playerChoice == "q":
                    break

            # otherwise if player has blackjack:
            elif self.hasBlackjack(player_obj):
                # Dealer tells player he has blackjack.
                print("You've got blackjack!")
                print("// -------------------------------")
                # remove player from playing players.
                self.remove(player_obj)

            # otherwise if player has won:
            elif self.won(player_obj):
                # Dealer tells player he is maxed out.
                print("You got 21! You're maxed, good luck!")
                print("// -------------------------------")
                # remove player from playing players.
                self.remove(player_obj)

            # otherwise if player has lost:
            elif self.lost(player_obj):
                # Print that player has lost and is out.
                print("Your total exceeded 21, you're out! You have lost.")
                print("// -------------------------------")
                # remove player
                self.remove(player_obj)
        # Make dealers final moves.
        self.playDealer()
        # Print winner.
        self.announceWinner()

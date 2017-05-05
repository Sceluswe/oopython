"""
A player class inheriting from Hand.
"""

import hand

class Player(hand.Hand):
    """
    The player class, contains name and bid.
    """
    highestBid = 0

    def __init__(self, str_playername):
        """
        Constructor.
        """
        super().__init__()
        self.str_playername = str_playername
        self.int_bid = 0

    def __eq__(self, other):
        """
        Equlaity operator: card == card
        """
        result = False

        if self.str_playername == other.str_playername:
            result = super().__eq__(other)

        return result

    def placeBet(self, int_number):
        """
        Increase your placed bid by int_number.
        """
        self.int_bid += int_number
        Player.highestBid = int_number

    def getBid(self):
        """
        Return current bid.
        """
        return self.int_bid

#!/usr/bin/env python3

"""
Blackjack test.
"""

import blackjack

playerChoice = input("How many players would you like? (Max 6)\n-->")

if playerChoice.isnumeric():
    if int(playerChoice) < 6 and int(playerChoice) > 0:
        myBlackJack = blackjack.Blackjack(int(playerChoice))
        print("// -------------------------------")
        myBlackJack.gameloop()
    else:
        print("Number must be: below 6 and above 0")
else:
    print("Amount of players must be numeric.")

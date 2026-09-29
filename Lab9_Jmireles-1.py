"""
The Main Game Logic
Janae Mireles
This file runs the game. It creates the player objects and manages the game loop and rules.
Spetember 28th, 2026
"""

from player import Player

def main():

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    play_again = 'y'

    while play_again == 'y' or play_again == 'Y':

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(player1.get_name(), "tossed", side1)
        print(player2.get_name(), "tossed", side2)

        if side1 == side2:

            player1.win_coin()
            player2.lose_coin()

            print(player1.get_name() "won the round!")
            


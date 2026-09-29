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

    print("--- Coin Match Game ---")
    print(player1.get_name(), "has", player1.get_wallet(), "coins.")  
    print(player2.get_name(), "has", player2.get_wallet(), "coins.")
    print()

    play_again = input("Do you want to toss the coins? (y/n): ")

    while play_again == 'y' or play_again == 'Y':

        print()
        print("Tossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(player1.get_name(), "tossed", side1)
        print(player2.get_name(), "tossed", side2)

        if side1 == side2:

            player1.win_coin()
            player2.lose_coin()

            print("...It's a match! Player 1 wins a coin.")

        else:

            player2.win_coin()
            player1.lose_coin()

            print("...No Match! Player 2 wins a coin.")

        print()
        print(player1.get_name(), "has", player1.get_wallet(), "coins.")
        print(player2.get_name(), "has", player2.get_wallet(), "coins.")
        print()

        play_again = input("Do you want to toss the coins? (y/n): ")

    print()
    print("--- Final Score ---")
    print("Player 1:", player1.get_wallet())
    print("Player 2:", player2.get_wallet())

    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 wins!")
    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 wins!")
    else:
        print("It's a draw!")

main()
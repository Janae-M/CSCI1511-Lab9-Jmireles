"""
The Coin Class
Janae Mireles
This is a class that represents a single tossable coin, based on heads or tails.
Spetember 28th, 2026
"""
import random

class Coin:
    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup
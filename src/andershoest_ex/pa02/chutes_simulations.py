# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

import random

class Board:
    ladder_dict = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
    snake_dict = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
    current_position = 0
    """
    Initializes the board.

    Creating a class of the board. Ladders and snakes represented by
    lists. Position 90 is the endpoint and position 0 is the start
    position.

    Arguments
    ---------
    param start : int 0
        The first position on the board.
    param goal : int 90
        the last position on the board.

    """

    def __init__(self, ladders=None, snakes=None, goal=90):
        self.ladders = ladders or Board.ladder_dict
        self.snakes = snakes or Board.snake_dict
        self.goal = goal

    def goal_reached(self, position):    # AH question: Method may be static?
        while not position >= 90:
            return False

    def position_adjustment(self, position):
        """
        Suggestion. subtract the value of the
        second index from the first in ladders/snakes
        numbers from test_base_pa02

        """
        changed_position = 0
        if position in self.ladders:
            return self.ladders[position] - position
        elif position in self.snakes:
            return self.snakes[position] - position
        return changed_position


class Player:    # AH: correct? or should it be Player(board)?

    def __init__(self, board):
        self.board = Board(Player)
        self.player = Player

    def move(self, throw_die):
        throw_die = random.randint(1, 6)
        return throw_die


if __name__ == "__main__":
    ladders = [(2, 7), (9, 25)]
    snakes = [(9, 2), (12, 3)]    # Ladders and snakes here?

# ladders position start position. End position
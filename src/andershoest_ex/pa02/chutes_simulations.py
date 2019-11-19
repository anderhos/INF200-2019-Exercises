# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

import random


class Board:
    # Ladder dictionary and snake dictionary from pa01
    ladder_dict = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
    snake_dict = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
    current_position = 0    # setting the starting position to zero

    def __init__(self, ladders=None, snakes=None, goal=90):
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
        self.ladders = ladders or Board.ladder_dict
        self.snakes = snakes or Board.snake_dict
        self.goal = goal

    def goal_reached(self, position):
        """
        Checks if goal is reached

        :param position:
        :return: bol
        """
        self.current_position = position
        # AH note. Skip previous line and use "position" instead?
        while not self.current_position >= 90:
            return False

    def position_adjustment(self, position):
        """
        The method takes as argument the position of the player
        and returns integer number of positions the player must move
        forward in case of a ladder or backward in case of a snake

        :param position
        :return: int
        """
        changed_position = 0
        if position in self.ladders:
            return self.ladders[position] - position
        elif position in self.snakes:
            return self.snakes[position] - position
        return changed_position


class Player:    # AH: correct? or should it be Player(board)? Test OK

    def __init__(self, board):
        """
        Initializes the player class.

        :param board
        """
        self.board = Board(Player)
        self.player = Player

    def move(self):
        Player.throw_die = random.randint(1, 6)


class ResilientPlayer(Player):

    def __init__(self, board, extra_steps):
        super().__init__(board)
        self.extra_steps = extra_steps

    def move(self):
        if Board.current_position in Board.snake_dict:
            return self.extra_steps
            # pytest: TypeError: __init__() missing 1 required
            # positional argument: 'extra_steps'

if __name__ == "__main__":
    ladders = [(2, 7), (9, 25)]
    snakes = [(9, 2), (12, 3)]    # Ladders and snakes here?

# ladders position start position. End position
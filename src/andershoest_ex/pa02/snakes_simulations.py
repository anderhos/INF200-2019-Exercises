# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'


class Board:
    """
    Initializes the board.

    Creating a class of the board. Ladders and snakes represented by
    lists. Position 90 is the endpoint and position 0 is the start
    position.

    Arguments
    ---------
    param start : int 0
        The first position on the boar.
    param goal : int 90
        the last position on the board.

    """

    def __init__(self, start, goal):
        self.current_position = start
        self.goal = 90

    def goal_reached(self):
        if self.current_position >= self.goal:
            return True

    def position_adjustment(self):
        """
        Suggstion. subtract the value of the
        second index from the first in ladders/snakes
        numbers from test_base_pa02

        """
        pass

if __name__ == "__main__":
    ladders = [(1, 4), (5, 16)]
    snakes = [(9, 2), (12, 3)]    # Ladders and snakes here?


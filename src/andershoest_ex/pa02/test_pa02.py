# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

import chutes_simulations as cs

class TestBoard:

    def test_goal_reached(self):
        """goal_reached() callable and returns bool"""
        b = cs.Board()
        assert isinstance(b.goal_reached(1), bool)

class TestPlayer:

    def test_first_move(self):
        """
        Testing the first move. The player position must be greater than
        the starting position at 0.
        """
        board = cs.Board()
        player = cs.Player(board)
        player.position = 0
        player.move()
        assert player.position > 0

    def test_snake(self):
        """
        Test that the position of the player must be less than the die
        after falling down a snake

        """
        board = cs.Board
        player = cs.Player(board)
        player.position = pos
        player.move()
        assert player.adjustment < 0

        # Error not done


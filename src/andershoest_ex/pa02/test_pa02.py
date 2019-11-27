# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

import chutes_simulations as cs

class TestPlayer:

    def test_change_position(self, position=0):
        """
        Testing that the position of the player must change after the player moves
        """
        board = cs.Board()
        player = cs.Player(board)
        initial_position = player.position
        player.move()
        new_position = player.position
        assert initial_position =! new_position

    def test_goal_reached(self):
        board = cs.Board
        player = cs.Player
        assert board.goal_reached()


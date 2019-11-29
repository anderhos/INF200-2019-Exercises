# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

import chutes_simulations as cs

class TestBoard:

    def test_snake_position(self):
        """
        test that the first snake in default board
        is on 24 and ends at position 5
        """
        board = cs.Board()
        assert board.snake_dict[24] == 5

    def test_ladder_position(self):
        """
        test that the first ladder in default board
        is on position 1 and that it ends on position 40

        """
        board = cs.Board()
        assert board.ladder_dict[1] == 40

    def test_goal_position(self):
        """
        test that the default board has goal on position 90

        """
        board = cs.Board()
        assert board.goal == 90

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


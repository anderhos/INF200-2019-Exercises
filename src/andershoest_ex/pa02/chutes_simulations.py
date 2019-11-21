# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

import random


class Board:
    # Ladder dictionary and snake dictionary from pa01
    ladder_dict = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
    snake_dict = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

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
        :return: bo
        """
        return position >= self.goal

        # AH note. Skip previous line and use "position" instead?


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
        self.board = board
        self.position = 0
        self.no_moves = 0    # Added number of moves
        self.adjustment = 0

    def move(self):
        if self.board.goal_reached(self.position):
            return
        throw_die = random.randint(1, 6)
        # number between 1 and 6
        new_temporary_pos = self.position + throw_die
        # move player to new position
        self.adjustment = self.board.position_adjustment(new_temporary_pos)
        # look for ladders or snakes
        self.position = new_temporary_pos + self.adjustment
        # changes position if adjustment is not 0.
        self.no_moves += 1    # Incrasing the number of moves


    def check_goal_reached(self):    # Added method check goal reached
        if self.board.goal_reached(self.position):
            return True


class ResilientPlayer(Player):

    def __init__(self, board, extra_steps=1):
        """
        Initializes ResilientPlayer as Subclass of Player.

        :param: board, extra_steps
        """
        super().__init__(board)
        self.extra_steps = extra_steps

    def move(self):    # AH note. Swich move with extra_steps?
        """
         return the extra steps taken after moving down a chute
        """
        if self.adjustment < 0:
            self.position += self.extra_steps
        super().move()


class LazyPlayer(Player):

    def __init__(self, board, dropped_steps=1):
        """
       Initializes ResilientPlayer as Subclass of Player.

       :param: board, dropped_steps
       """
        super().__init__(board)
        self.dropped_steps = dropped_steps

    def move(self):
        """
        Return dropped steps after moving up a ladder
        dropped steps cannot be less than the dice throw
        :return: dropped_steps
        """
        if self.adjustment > 0:
            old_position = self.position

            self.position = old_position - self.dropped_steps
            super().move()
            die = self.position - old_position + self.dropped_steps\
                  - self.adjustment
            if die < self.dropped_steps:
                self.position = old_position
        else:
            super().move()



        """
        if self.adjustment > 0:
            if self.position - self.dropped_steps >
                self.position -= self.dropped_steps
        super().move()
        """

        """
        Player.throw_die = random.randint(1, 6)
        if Board.current_position in Board.ladder_dict:
            while not Player.throw_die < self.dropped_steps:
                return self.dropped_steps
        else:
            return Board.current_position == Board.current_position
        """

class Simulation:

    def __init__(self, player_field, board=None,  seed=1234,
                 randomize_players=True):
        """
        Initialize the Simulation class to manage simulations of the game

        :param: board,
        :param: seed,
        :param: randomize_players,
        :param: player_field
        AH. note. Two first tests OK

        """
        self.board = board or Board()
        self.seed = seed
        self.randomize_players = randomize_players
        self.player_field = player_field

    def single_game(self):
        """
        Runs a single game, returning a tuple consisting the number of moves
        used to win the game and the type of the winner.

        Using code from pa01

        :param:

        Making a list of player instances for the different player types.

        """

        player_list = [player_class(self.board)
                       for player_class in self.player_field]

        position_list = [0 for _ in player_list]
        moves_list = [0 for _ in player_list]

# Loop


    def run_simulation(self):
        """
        run a given number of games and stores the results in the Simulation
        object.
        :param:

        """

        pass

    def get_results(self):
        """
        Return all the results generated by run_simulation as a tuple with
        the number of games won by different types

        """
        pass


if __name__ == "__main__":
    board = Board()
    resilient_player = ResilientPlayer(board)
    for _ in range(40):
        resilient_player.move()
        print(resilient_player.position)



# Notes AH. Dont need a main
# Write own tests at least one for each method
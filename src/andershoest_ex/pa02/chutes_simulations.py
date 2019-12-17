# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
Note from author: I did not manage to implement all the functions.

"""

import random
from collections import Counter


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
        # Stop moving after the goal is reached
        throw_die = random.randint(1, 6)
        # number between 1 and 6
        new_temporary_pos = self.position + throw_die
        # move player to new position
        self.adjustment = self.board.position_adjustment(new_temporary_pos)
        # look for ladders or snakes
        self.position = new_temporary_pos + self.adjustment
        # changes position if adjustment is not 0.
        self.no_moves += 1    # Increasing the number of moves

    def check_goal_reached(self):    # Added method check goal reached
        if self.board.goal_reached(self.position):
            return True


class ResilientPlayer(Player):

    def __init__(self, board, extra_steps=5):
        """
        Initializes ResilientPlayer as Subclass of Player.

        :param: board, extra_steps
        """
        super().__init__(board)
        self.no_moves = 0
        self.extra_steps = extra_steps

    def move(self):    # AH note. Swich move with extra_steps?
        """
         return the extra steps taken after moving down a chute
        """
        if self.adjustment < 0:
            self.position += self.extra_steps
        super().move()
        self.no_moves += 1
        # Do the regular move


class LazyPlayer(Player):

    def __init__(self, board, dropped_steps=5):
        """
       Initializes ResilientPlayer as Subclass of Player.

       :param: board, dropped_steps
       """
        super().__init__(board)
        self.no_moves = 0
        self.dropped_steps = dropped_steps

    def move(self):
        """
        Return dropped steps after moving up a ladder
        dropped steps cannot be less than the dice throw
        :return: dropped_steps
        """
        if self.adjustment > 0:
            # The player moves up a ladder
            old_position = self.position
            # In the next move, player on top of ladder

            self.position = old_position - self.dropped_steps
            # player drops steps
            super().move()
            # player move
            self.no_moves += 1
            # update number of moves
            die = self.position - old_position + self.dropped_steps - \
                self.adjustment
            """ 
            the current position of the player is: old position - 
            dropped_steps + die + adjustment. Rearranging to find the die.
            
            """
            if die < self.dropped_steps:
                self.position = old_position
            # if die is less than dropped_steps, the player will stand still.
        else:
            super().move()
            # if not climbling a ladder, then the player make a regular move

class Simulation:

    def __init__(self, player_field=None, board=None,  seed=1234,
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
        random.seed(seed)    # note AH: What does this line actually do?
        self.randomize_players = randomize_players
        self.player_field = player_field or [Player, Player]
        self.result = []

    def randomize(self):
        """
        defining a function to shuffle the players in randomly order

        """
        if self.randomize_players is True:
            random.shuffle(self.player_field)

    def single_game(self):
        """
        Runs a single game, returning a tuple consisting the number of moves
        used to win the game and the type of the winner.

        Using code from pa01

        :param:

        Making a list of player instances for the different player types.

        """
        self.randomize()
        player_list = [player_class(self.board)
                       for player_class in self.player_field]
        # Making a list of players of different classes in a single game
        no_moves = 0
        # All players make moves as long as the game is not finished
        while True:
            for player in player_list:
                player.move()
                no_moves += 1
                if self.board.goal_reached(player.position):
                    # Last line returning the number of moves of the class
                    # instance that won the game,
                    #  and the name of that type.
                    return player.no_moves, type(player).__name__

    def run_simulation(self, num_games=10):
        """
        run a given number of games and stores the results in the Simulation
        object.
        :param:

        """
        for _ in range(num_games):
            self.result.append(self.single_game())

    def get_results(self):
        """
        Return all the results generated by run_simulation as a tuple with
        the number moved made by the winner

        """
        return self.result

    def winners_per_type(self):
        """
        Returns a dictionary mapping player types to the number of wins
        with the key representing the player type and the value the
        number of wins for that specific type.

        :return:
        """
        winners = [winner[1] for winner in self.result]
        # making a list of the type of winners
        return Counter(winners)
        # Using the Counter tool from the standard library to count the
        # types in a dictionary

    def convert(self, tuples, dictionary):
        """
        Defining a function to convert result tuples into a dictionary
        Source:
        https://www.geeksforgeeks.org/python-convert-list-tuples-dictionary/

        """
        for a, b in tuples:
            dictionary.setdefault(b, []).append(a)
            # Changing key and value positions
            # Set default returns value of the key if it is in the dictionary
            # Otherwise it inserts key with value
        return dictionary

    def durations_per_type(self):
        """
        Returning a dictionary mapping player types to lists of game durations
        a dictionary of lists with the player type as key and the game
        durations for that specific type as a list of values

        """
        temp_dict = {}
        # Creating an empty dictionary
        dict_durations = self.convert(self.result, temp_dict)
        return dict_durations

        # appending durations




if __name__ == "__main__":
    sim = Simulation(player_field=[Player, LazyPlayer, ResilientPlayer],
                     randomize_players=True)
    sim.run_simulation(20)
    results = sim.result
    win_per_type = sim.winners_per_type()
    dur_per_type = sim.durations_per_type()
    print(results)
    print(win_per_type)
    print(dur_per_type)
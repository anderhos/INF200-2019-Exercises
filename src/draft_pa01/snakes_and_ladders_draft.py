class Board:
    def __init__(self):
        self.board = [None]*90    # 90 positions on board
    def is_ladder(self, position):
        """
        Returns True if the position is ladder
        """
        """
        Defining a dictionary for ladders
        Keys: From	1	8	36	43	49	65	68
        Values: To	40	10	52	62	79	82	85
        Correct?
        """
        ladder_dict = {
            1 : 40,
            8: 10,
            36: 52,
            43: 62,
            49: 79,
            65: 82,
            68: 85,
        }
        if position in ladder_dict:
            return value
    else
    def is_snake(self.position):
        """
        Returns True if the position is snake
        """

    def is_regular(self.position)
        """ 
        Returns True if the position is a regular position
        """
def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """



def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """

def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """
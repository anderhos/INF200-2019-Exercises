# -*- coding: utf-8 -*-

from walker_sim import Walker, Simulation

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'


class BoundedWalker(Walker):

    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
         """
        super().__init__(start, home, seed)
        BoundedWalker.right_limit = right_limit
        BoundedWalker.left_limit = left_limit


if __name__ == "__main__":
    left_boundaries = [0, -10, -100, -1000, -10000]
    for i in left_boundaries:
        bounded_sim_1 = BoundedSimulation(0, 20, 12345, i, 20)
        print("Left boundary:", i, "-->", "Walk durations:",
              bounded_sim_1.run_simulation(20))





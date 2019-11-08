# -*- coding: utf-8 -*-

import random
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
        self.start = start
        self.left_limit = left_limit
        self.right_limit = right_limit

<<<<<<< HEAD
    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """

        bounded_walker = BoundedWalker(self.current_position, self.home,
                                       self.left_limit, self.right_limit)
        while not bounded_walker.is_at_home():
            bounded_walker.direction = random.randint(0, 1)
            if bounded_walker.direction == 0 and \
                    bounded_walker.current_position == left_boundaries:
                continue
            elif bounded_walker.direction == 1 and \
                    bounded_walker.current_position == right_boundary:
                continue
            else:
                bounded_walker.move()
        return bounded_walker.get_steps()
=======
>>>>>>> parent of e65b8fb... Making ready for delivery. Did not manage all ex

if __name__ == "__main__":
    left_boundaries = [0, -200]
    right_boundary = 20
    for i in left_boundaries:
        bounded_sim_1 = BoundedSimulation(0, 20, 12345, i, right_boundary)
        print("Left boundary:", i, "-->", "Walk durations:",
<<<<<<< HEAD
              bounded_sim_1.run_simulation(5))
=======
              bounded_sim_1.run_simulation(20))


>>>>>>> parent of e65b8fb... Making ready for delivery. Did not manage all ex



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

    def move(self):
        super().move()
        if self.get_position() < self.left_limit:
            self.current_position = self.left_limit
        elif self.get_position() > self.right_limit:
            self.current_position = self.right_limit


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
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_walk(self):
        bounded_walker = BoundedWalker(self.current_position, self.home,
                                       self.left_limit, self.right_limit)
        while not bounded_walker.is_at_home():
            bounded_walker.move()
        return bounded_walker.get_steps()


if __name__ == "__main__":
    left_boundaries = [0, -10, -100, -1000, -10000]
    right_boundary = 20
    for left_boundary in left_boundaries:
        bounded_sim_1 = BoundedSimulation(0, 20, 12345, left_boundary,
                                          right_boundary)
        print("Left boundary:", left_boundary, "-->", "Walk durations:",
              bounded_sim_1.run_simulation(20))

# -*- coding: utf-8 -*-

import random

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'


class Walker:

    def __init__(self, start, home):
        """
    :param start: initial position of the walker
    :param home: position of the walker's home
    """
        self.current_position = start
        self.home = home
        self.steps_taken = 0

    def get_position(self):
        """Returns current position."""
        x = self.current_position
        return x

    def get_steps(self):
        """Returns number of steps taken by walker."""
        return self.steps_taken

    def is_at_home(self):
        """Returns True if walker is at home position."""
        return self.current_position == self.home

    def move(self):
        """
        Change coordinate by +1 or -1 with equal probability.
        """
        x = random.randint(0, 1)
        if x == 0:
            self.current_position -= 1
        else:
            self.current_position += 1
        self.steps_taken += 1


class Simulation:

    def __init__(self, start, home, seed):
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
        """
        self.current_position = start
        self.home = home
        random.seed(seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        walker = Walker(self.current_position, self.home)
        while not walker.is_at_home():
            walker.move()
        return walker.get_steps()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """

        return [self.single_walk() for _ in range(num_walks)]


if __name__ == "__main__":

    sim_1 = Simulation(0, 10, 12345)
    print("Steps taken by the walker from starting position 0 to home position"
          " 10 over 20 walks with seed 12345", sim_1.run_simulation(20))

    sim_2 = Simulation(0, 10, 12345)
    print("Steps taken by the walker from starting position 0 to home position"
          " 10 over 20 walks with seed 12345 as above",
          sim_2.run_simulation(20))

    sim_3 = Simulation(10, 0, 12345)
    print("Steps taken by the walker from starting position 10 to home "
          "position 0 over 20 walks with seed 12345",
          sim_3.run_simulation(20))

    sim_4 = Simulation(10, 0, 12345)
    print("Steps taken by the walker from starting position 10 to "
          "home position 10 over 20 walks with seed 12345 as above",
          sim_4.run_simulation(20))

    sim_5 = Simulation(0, 10, 54321)
    print("Steps taken by the walker from starting position 0 to home position"
          " 10 over 20 walks with seed 54321",
          sim_5.run_simulation(20))

    sim_6 = Simulation(10, 0, 54321)
    print("Steps taken by the walker from starting position 10 to "
          "home position 10 over 20 walks with seed 54321 as above",
          sim_6.run_simulation(20))

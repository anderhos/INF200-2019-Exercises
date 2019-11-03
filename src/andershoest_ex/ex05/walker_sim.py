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
        self.seed = seed

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

     #empty list, append

    # list_steps = [0] * 20
    # list_simulations = [list_steps] * 6

   # sim1 = Simulation(0, 10, 12345)
   # sim2 = Simulation(0, 10, 12345)
    # sim3 = Simulation(10, 0, 12345)
    #sim4 = Simulation(10, 0, 12345)
    #sim5 = Simulation(0, 10, 54321)
    #sim6 = Simulation(10, 0, 54321)
    #simulations = [sim1, sim2, sim3, sim4, sim5, sim6]

    data = [[0, 10, 12345], [0, 10, 12345], [10, 0, 12345], [10, 0, 12345],
        [0, 10, 54321], [10, 0, 54321]]

    for a, b, c in data:
        list_steps = [0] * 20
        list_simulations = [list_steps] * 6
        for i in range(6):
            sim = Simulation(a, b, c)
            list_steps[i] = sim.run_simulation(20)



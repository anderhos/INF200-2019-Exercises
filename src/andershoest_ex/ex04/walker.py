# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'


import random


class Walker:
    steps_taken = 0

    def __init__(self, x0, h):
        self.current_position = x0
        self.h = h

    def move(self):
        x = random.randint(0, 1)
        if x == 0:
            self.current_position -= 1
        else:
            self.current_position += 1
        self.steps_taken += 1

    def is_at_home(self):
        if self.current_position != self.h:
            return False

    def get_position(self):
        x = self.current_position
        return x

    def get_steps(self):
        return self.steps_taken


if __name__ == "__main__":
    for j in (1, 2, 5, 10, 20, 50, 100):
        steps = [0] * 5
        for i in range(5):
            walker = Walker(0, j)
            while not walker.is_at_home():
                walker.move()
            steps[i] = walker.get_steps()
        print("Distance: ", j, " --> Path length: ", steps)

# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'


import random

class Walker:
    def __init__(self, steps, current_position, h):
        self.steps = 0
        self.current_position = current_position
        self.h = h

    def move(self):
        x = random.randint (0, 1)
        if x == 0:
            self.start_position -= 1
        else:
            self.start_position += 1

    def is_at_home(self):
        if self.current_position == self.h:
            return True

    def get_position(self):
        return self.current_position

    def get_steps(self):
        return self.steps





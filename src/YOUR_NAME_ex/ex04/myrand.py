# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'


# Implementing the first random number generator class
class LCGRand:
    def __init__(self, seed):
        self.seed = seed

# Generate numbers according to equation
    def rand(self):
        a = 7 ** 5
        m = 2 ** 31 - 1
        self.seed = a * self.seed % m
        return self.seed


# Implementing the second random number generator class
class ListRand:
    def __init__(self, numbers_list):
        self.numbers_list = numbers_list
        self.index = -1    # Adjusting the index

    def rand(self):
        self.index = self.index + 1
        if self.index < len(self.numbers_list):
            return self.numbers_list[self.index]
        else:
            raise RuntimeError


if __name__ == "__main__":
    number1 = 4    # Defining a number for LCGRand
    numbers_list = [1, 2, 3]    # Defining a list of numbers for ListRand
    for numbers_list in ListRand
        print(numbers_list.rand())    # Printing numbers, NOT WORKING
    # How to proceed?

# Checkout examples online
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

    def __len__(self):
        return len(self.numbers_list)


if __name__ == "__main__":
    number_1 = LCGRand(1)    # Defining a number input into LCGRand
    list_input = ListRand([4, 3, 6, 9, 24])    # Defining a list of numbers for
    # ListRand
    for index in range(5):
        print(number_1.rand())

    for index in range(len(list_input)):
        print(list_input.rand())
    try:
        list_input.rand()
    except RuntimeError:
        print("Last number has been delivered!")

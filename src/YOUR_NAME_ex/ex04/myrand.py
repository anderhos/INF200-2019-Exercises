# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'


class LCGRand:

    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        a = 7 ** 5
        m = 2 ** 31 - 1
        self.seed = a * self.seed % m
        return self.seed


class ListRand:
    def __init__(self, numbers_list):
        self.numbers_list = numbers_list
        self.index = -1

    def rand(self):
        self.index = self.index + 1
        if self.index < len(self.numbers_list):
            return self.numbers_list[self.index]
        else:
            raise RuntimeError


if __name__ == "__main__":
    print(LCGRand(5))
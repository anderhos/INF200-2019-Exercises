__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

# INF200 ex01
# Task B
# Create loop from list comprehension


#  Defining squares by list comprehension


def squares_by_comp():
    return [k**2 for k in range(n) if k % 3 == 1]

# Defining squares by using a for-loop


def squares_by_loop():
    squares = []
    for k in range(n):
        if k % 3 == 1:
            squares.append(k ** 2)
    return squares


"""Checking if the two functions squares_by_comp(n) and squares_by_loop()
 returns the same value"""


if __name__ == '__main__':
    n = 50  # adding an input value for n
    if squares_by_loop() != squares_by_comp():
        print('ERROR!')

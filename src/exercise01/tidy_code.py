__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

# INF200 ex01
# Task C
# Clean up code

from random import randint as ran

# Guessing the number of two dices


def guessing_game():
    guess_a_number = 0
    while guess_a_number < 1:
        guess_a_number = int(input('Your guess: '))
    return guess_a_number


# Throw two dice


def throw_dices():
    return ran(1, 6) + ran(1, 6)


def check_guess(your_guess, your_dice):
    return your_guess == your_dice


if __name__ == '__main__':

    has_won = False
    number_of_guesses_left = 3
    dice = throw_dice()
    while not has_won and number_of_guesses_left > 0:
        guess = guessing_game()
        has_won = check_guess(dices, guess)
        if not has_won:
            print('Wrong, try again!')
            number_of_guesses_left -= 1

    if number_of_guesses_left > 0:
        print('You won {number_of_guesses_left} points.')
    else:
        print('You lost. Correct answer: {your_dice}.')

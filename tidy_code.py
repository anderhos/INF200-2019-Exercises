from random import randint as ran

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

# Guessing the number of two dices


def guessing_game():
    guess_a_number = 0
    while guess_a_number < 1:
        guess_a_number = int(input('Your guess: '))
    return guess_a_number


# Throw two dices


def throw_dices():
    return ran(1, 6) + ran(1, 6)


def check_guess(your_guess, your_dices):
    return your_guess == your_dices


if __name__ == '__main__':

    is_not_true = False
    i = 3
    dices = throw_dices()
    while not is_not_true and i > 0:
        guess = guessing_game()
        is_not_true = check_guess(dices, guess)
        if not is_not_true:
            print('Wrong, try again!')
            i -= 1

    if i > 0:
        print('You won {} points.'.format(i))
    else:
        print('You lost. Correct answer: {}.'.format(dices))
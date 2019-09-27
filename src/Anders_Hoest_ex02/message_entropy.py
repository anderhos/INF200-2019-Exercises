__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'
"""
INF200 
EX 02 
Task B
"""


from collections import Counter, defaultdict

import math

# The letter frequency function from ex 01, task C.


def letter_freq(txt):
    return Counter(txt.lower())


def entropy(message):
    message_freq = letter_freq(message)
    letters_total = 0    # Total number of letters in message, N
    for i in message_freq.values():
        letters_total += i
    ent = 0
    for i in message_freq.values():    # Using the formula for entropy
        ent = ent + (i / letters_total)\
              * math.log((i / letters_total), 2)

    return -1 * ent


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))

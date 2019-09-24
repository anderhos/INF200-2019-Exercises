__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

# INF200 ex01
# Task A
# Create a card deck by list comprehension

# Creating suits and values for cards
SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


# Creating the card deck by using a for-loop
def deck_loop():
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


# Creating the card deck by list comprehension
deck_comp = [(suit, val) for suit in SUITS for val in VALUES]


# Checking if the two card decks are the same
if __name__ == '__main__':
    if deck_loop() != deck_comp:
        print('ERROR!')

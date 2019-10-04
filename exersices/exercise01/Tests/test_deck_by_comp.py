
from deck_by_comp import deck_comp


def test_deck_of_cards_have_52_cards():
    assert len(deck_comp()) == 52


def test_deck_of_cards_have_four_suits():
    deck = deck_comp()
    suits = {suit for suit, value in deck}    # Set. Like a list, but all
    # duplicates are deleted
    assert len(suits) == 4


# Create a test to check if there are 13 values


def test_deck_of_cards_have_13_values():
    deck = deck_comp()
    values = {value for value, value in deck}    # Set
    assert len(values) == 13

# Create a test to check if there are 52 unique cards


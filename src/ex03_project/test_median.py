# -*- coding: utf-8 -*-
import pytest


__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

# INF200. Ex_03-Task B


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    if n == 0:
        raise ValueError
    return (sdata[n//2] if n % 2 == 1
            else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


# Testing if the function returns the correct value for a one-element list


def test_single():
    data1 = [1]
    assert median(data1) == 1


# Testing if the function returns the correct value for a odd numbered list


def test_list_odd():
    data2 = [1, 3, 5, 7, 9]
    assert median(data2) == 5


# Testing if the function returns the correct value for an even numbered list


def test_list_even():
    data3 = [2, 4, 6, 8, 10]
    assert median(data3) == 6


"""
Testing if the function returns the correct value for an ordered numbered 
list
"""


def test_list_ordered():
    data4 = [1, 2, 3, 4, 5]
    assert median(data4) == 3


"""
Testing if the function returns the correct value for a reversed 
list
"""


def test_list_reverse():
    data5 = [5, 4, 3, 2, 1]
    assert median(data5) == 3


"""
Testing if the function returns the correct value for an unordered numbered 
list
"""


def test_list_unordered():
    data6 = [6, 9, 11, 2, 4]
    assert median(data6) == 6


# Testing the function for an empty list


def test_list_empty():
    with pytest.raises(ValueError) as err:
        median([])
    assert err.type is ValueError


# Testing if the function keeps the original list unchanged


def test_original_unchanged():
    data8 = [3, 2, 1, 9, 10]
    median(data8)
    assert data8 == [3, 2, 1, 9, 10]


# Testing if the function returns the correct value for both lists and tuples


def test_if_function_works_for_tuples_and_lists():
    data_list = [4, 5, 6, 1, 2]
    data_tuple = (2, 4, 9, 5, 6)
    assert median(data_list) == 4
    assert median(data_tuple) == 5

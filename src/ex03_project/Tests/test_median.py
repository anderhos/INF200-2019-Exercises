# -*- coding: utf-8 -*-

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
    return (sdata[n//2] if n % 2 == 1
        else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


def test_single():
    data1 = [1]
    assert median(data1) == 1


def test_list_odd():
    data2 = [1, 3, 5, 7, 9]
    assert median(data2) == 5
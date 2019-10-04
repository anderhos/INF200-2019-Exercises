# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

# INF200. Ex_03-Task A


def bubble_sort(dataset):
    list_dataset = list(dataset)
    length_list_dataset = len(list_dataset)

    # Looping through the entire list of numbers
    for i in range(0, length_list_dataset):
        for j in range(0, length_list_dataset - i - 1):
            # If the number in the next position is smaller than the current
            # Switch positions
            if list_dataset[j] > list_dataset[j+1]:
                list_dataset[j], list_dataset[j+1] = \
                    list_dataset[j+1], list_dataset[j]

    return list_dataset


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([0])


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data1 = [3, 2, 1]
    sorted_data = bubble_sort(data1)
    assert sorted_data != data1


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data1 = [3, 2, 1]
    sorted_data = bubble_sort(data1)
    assert sorted_data == [1, 2, 3]
    assert data1 == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data1 = [3, 2, 1]
    sorted_data = bubble_sort(data1)
    sort_sorted_data = bubble_sort(sorted_data)
    assert sort_sorted_data == [1, 2, 3]


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data1 = [3, 2, 1]
    sorted_data = bubble_sort(data1)
    assert sorted_data == [1, 2, 3]


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data2 = [1, 1, 1]
    sorted_data = bubble_sort(data2)
    assert sorted_data == [1, 1, 1]


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    numbers = [7, 3, 2, 4, 9]
    strings = ['st', 'ab', 'rs', 'qu']
    sorted_numbers = bubble_sort(numbers)
    sorted_strings = bubble_sort(strings)
    assert sorted_numbers == [2, 3, 4, 7, 9]
    assert sorted_strings == ['ab', 'qu', 'rs', 'st']

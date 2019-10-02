__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'
"""
INF200 
EX 02 
Task C
"""


def bubble_sort(dataset):
    # Creating a new list
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

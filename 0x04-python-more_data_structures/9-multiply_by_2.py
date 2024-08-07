#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2.

    """
    b_dictionary = {}
    for x, y in a_dictionary.items():
        y = y * 2
        b_dictionary[x] = y

    return b_dictionary

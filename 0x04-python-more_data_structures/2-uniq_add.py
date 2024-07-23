#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""

    [total += 1 for x in my_list if x is not in my_list]
    return total


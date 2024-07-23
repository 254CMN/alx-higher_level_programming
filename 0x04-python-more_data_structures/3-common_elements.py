#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Returns a set of common elements from two sets"""

    set_3 = {x  for x in set_1 for y in set_2 if x == y and  x in set_2}

    return set_3


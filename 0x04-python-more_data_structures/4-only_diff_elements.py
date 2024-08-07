#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set"""

    set_a = {x for x in set_1 for y in set_2 if x not in set_2}
    set_b = {y for x in set_1 for y in set_2 if y not in set_1}
    set_c = set_a | set_b

    return set_c


#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer.

    """
    max_value = max(a_dictionary, key=a_dictionary.get)
    for key, data in a_dictionary.items():
        if data == max_value:
            return key
        else:
            return None

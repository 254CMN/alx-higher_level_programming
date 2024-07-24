#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary.

    """
    for i in a_dictionary.keys():
        if key in i:
            del a_dictionary[key]
        else:
            return a_dictionary
    return a_dictionary

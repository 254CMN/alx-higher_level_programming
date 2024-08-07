#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary

    """
    for i in a_dictionary.keys():
        if key in i:
            a_dictionary[key] = value

    if key not in a_dictionary.keys():
        a_dictionary[key] = value

    return a_dictionary

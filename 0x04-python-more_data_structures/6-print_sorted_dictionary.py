#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys

    """
    sorted_dic = sorted(a_dictionary)
    
    for i in sorted_dic:
        print(i,":", a_dictionary.get(i))


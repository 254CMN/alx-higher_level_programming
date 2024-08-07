#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
#my_dict = { 'languages': “C”, ‘number’: 13, ‘track’: “Low level” }
#my_dict = { ‘a’: “a”, ‘b’: “b” , ‘c’: “c”, ‘d’: “d”, ‘e’: “e” }
#my_dict = { ‘languages’: “C” }
#my_dict = { }
print_sorted_dictionary(a_dictionary)


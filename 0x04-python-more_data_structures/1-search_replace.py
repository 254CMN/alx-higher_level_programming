#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by another in a new list"""

    new_list = []
    for nums in my_list:
        if nums == search:
            search = replace
        new_list.append(nums)

    return new_list


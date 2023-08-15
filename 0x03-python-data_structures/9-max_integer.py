#!/usr/bin/python3

def max_integer(my_list=[]):

    # Check if the list is empty, and if so, return None.
    if not my_list:
        return None

    # Initialize a variable to store the maximum item.
    max_item = my_list[0]

    # Iterate through the list to find the maximum item.
    for item in my_list:
        if item > max_item:
            max_item = item
    return max_item

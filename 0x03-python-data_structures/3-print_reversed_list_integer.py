#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    # Check if the list is empty or not provided.
    if not my_list:
        return

    # Create a copy of the input list and reverse it.
    rev = my_list[:]
    rev.reverse()

    # Iterate through the reversed list and print each element as an integer.
    for item in rev:
        print("{:d}".format(item))

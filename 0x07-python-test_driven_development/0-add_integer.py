#!/usr/bin/python3

""" Module defines a function to add two integers """


def add_integer(a, b=98):
    """ Adds two integers """

    # Check if 'a' is not an integer or float, & raise a TypeError if its not.
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    # Check if 'b' is not an integer or float, and raise a TypeError if its not
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    # Convert 'a' and 'b' to integers and return their sum.
    return int(a) 

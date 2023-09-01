#!/usr/bin/python3

""" Module defines a function to print a square made of '#' characters """


def print_square(size):
    """ Defines a function named print_square that takes the parameter size"""

    """
    Check if the "size" parameter is not an integer and 
    raise a TypeError if it's not.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    """
    # Check if the "size" parameter is less than 0 and 
    raise a ValueError if it is.
    """
    if size < 0:
        raise ValueError("size must be >= 0")
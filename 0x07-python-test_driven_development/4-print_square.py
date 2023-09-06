#!/usr/bin/python3
""" Defines a function thats prints a square."""


def print_square(size):
    """
    Print a square with the # character.
    Takes only one argument: size.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

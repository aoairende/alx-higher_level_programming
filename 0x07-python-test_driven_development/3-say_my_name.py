#!/usr/bin/python3
""" Defines a function thats prints a name."""


def say_my_name(first_name, last_name=""):
    """
    Prints a name.
    Takes two arguments: first_name and last_name.  
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3

""" Module defines a function """

"""
Define a function named "say_my_name" 
that takes two parameters, "first_name" and "last_name".
"""
def say_my_name(first_name, last_name=""):
    """Print first and last name"""

    """
    Check if the "first_name" parameter is not a string 
    and raise a TypeError if it's not.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    """
    # Check if the "last_name" parameter is not a string and 
    raise a TypeError if it's not.
    """
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

     # Print a message with the first and last name provided as parameters.
    print(f"My name is {first_name} {last_name}")

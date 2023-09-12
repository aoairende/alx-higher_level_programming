#!/usr/bin/python3

""" Defines a function that checks class. """


def is_same_class(obj, a_class):
    """ Checks class instance
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """

    return True if type(obj) == a_class else False

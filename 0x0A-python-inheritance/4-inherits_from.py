#!/usr/bin/python3

""" Defines a function. """


def inherits_from(obj, a_class):
    """ Checks class instance inherited
    obj: an object.
    a_class: a class.
    Returns: None
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class

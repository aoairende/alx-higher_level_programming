#!/usr/bin/python3
""" Defines a function that adds attributes to objects."""


def add_attribute(obj, attribute, value):
    """ Add attribute to an object """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)

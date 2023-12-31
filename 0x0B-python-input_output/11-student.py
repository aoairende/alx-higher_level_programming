#!/usr/bin/python3

""" Defines a class. """


class Student:
    """ Student class. """

    def __init__(self, first_name, last_name, age):
        """ Initialises an instance. """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ A dictionary representation of a Student instance. """

        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attribute of Student instance. """

        for key, value in json.items():
            setattr(self, key, value)

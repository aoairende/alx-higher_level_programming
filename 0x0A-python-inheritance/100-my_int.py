#!/usr/bin/python3
""" Defines a class that inherits from int. """


class MyInt(int):
    """ Class extends int """

    def __eq__(self, value):
        """ Implemented as != """

        return self.real != value

    def __ne__(self, value):
        """ Implemented as == """

        return self.real == value

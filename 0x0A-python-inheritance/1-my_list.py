#!/usr/bin/python3

""" Defines a class. """


class MyList(list):
    """ Represents list class MyList. """

    def print_sorted(self):
        """ Prints the sorted list. """

        print(sorted(self))

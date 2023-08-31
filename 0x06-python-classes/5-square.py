#!/usr/bin/python3
""" Defines a square class """


class Square:
    """ Defines a square class """

    def __init__(self, size=0):
        """Initializes a new square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Returns the area of the square """

        return self.__size * self.__size

    @property
    def size(self):
        """ Returns size of the square """

        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the value of size """

        self.__init__(value)

    def my_print(self):
        """ Prints square using the # """

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print(self.__size * "#")

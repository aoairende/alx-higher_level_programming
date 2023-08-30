#!/usr/bin/python3
""" Defines a square class """


class Square:
    """ Defines a square class """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a new square """

        self.size = size
        self.position = position

    def area(self):
        """ Returns the area of the square """

        return self.__size * self.__size

    @property
    def size(self):
        """ Returns the size of the square """

        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Returns the position of the square """

        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the value of position """

        if not (
            isinstance(value, tuple)
            and len(value) == 2
            and isinstance(value[0], int)
            and isinstance(value[1], int)
            and value[0] >= 0
            and value[1] >= 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Prints square using the # """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(self.__position[0] * " ", end="")
                print(self.__size * "#")

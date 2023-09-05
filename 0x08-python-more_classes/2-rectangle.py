#!/usr/bin/python3

# Module defines a class named Rectangle
class Rectangle:

    # Constructor method for Rectangle class
    def __init__(self, width=0, height=0):

        # Initialize width and height attributes
        self.width = width
        self.height = height

    # Getter method for the 'width' property
    @property
    def width(self):

        return self.__width

    # Setter method for the 'width' property
    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Getter method for the 'height' property
    @property
    def height(self):

        return self.__height

    # Setter method for the 'height' property
    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Calculate the area of the rectangle
    def area(self):

        return self.__width * self.__height

    # Calculate the perimeter of the rectangle
    def perimeter(self):

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

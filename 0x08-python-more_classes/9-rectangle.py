#!/usr/bin/python3
""" Module defines a class named Rectangle """


class Rectangle:

    """ Class variables to keep track of the number of instances """
    number_of_instances = 0
    print_symbol = "#"

    """ Constructor method for Rectangle class """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    """ Getter method for the 'width' property """
    @property
    def width(self):

        return self.__width

    """ Setter method for the 'width' property """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Getter method for the 'height' property """
    @property
    def height(self):

        return self.__height

    """ Setter method for the 'height' property """
    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ calculate the area of the rectangle """
    def area(self):

        return self.__width * self.__height

    """ calculate the perimeter of the rectangle """
    def perimeter(self):

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    """ string representation for the rectangle """
    def __str__(self):
        string = ""

        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            string += f"{self.__width * self.print_symbol}\n"
        return string.strip("\n")

    def __repr__(self) -> str:
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):

        return cls(size, size)

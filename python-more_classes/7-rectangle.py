#!/usr/bin/python3

"""
A class that defines any rectangle
"""


class Rectangle:

    """
    Rectangle class with a positive integer width and height
    and area/perimeter available.
    Width/height getter and setter included.
    The rectangle can be printed with a string representation.
    Deleting the rectangle leaves a message.
    The number of instances are counted.
    Printed symbol can be changed.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = self.print_symbol

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        string = ""
        if (self.__width != 0) and (self.__height != 0):
            for i in range(self.__height):
                for j in range(self.__width):
                    string += "{}".format(Rectangle.print_symbol)
                if i != self.__height - 1:
                    string += "\n"
        return string

    def print(self):
        print(Rectangle.__str__(self))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

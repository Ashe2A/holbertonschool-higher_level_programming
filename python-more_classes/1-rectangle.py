#!/usr/bin/python3

"""
A class that defines any rectangle
"""


class Rectangle:

    """
    Rectangle class with a positive integer width and height.
    and area available. Width/height getter and setter included.
    The rectangle can be printed with a specified spacing position.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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

    def my_print(self):
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()

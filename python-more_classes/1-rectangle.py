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

    def __init__(self, width=0, height=0, position=(0, 0)):
        self.width = width
        self.height = height
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple))\
            or (len(position) != 2)\
            or (not isinstance(position[0], int))\
                or (not isinstance(position[1], int))\
                or (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__width * self.__height

    def my_print(self):
        if (self.__height == 0):
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__height):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print()

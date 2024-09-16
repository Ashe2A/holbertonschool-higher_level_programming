#!/usr/bin/python3

"""
A class that defines any square
"""


class Square:

    """
    Square class with a positive integer size
    and area available. Size getter and setter included.
    The square can be printed with a specified spacing position.
    """

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (not isinstance(position()[0], int))\
            or (not isinstance(position()[0], int))\
            or (position()[0] < 0) or (position()[1] < 0):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.size() * self.size()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        for i in range(self.position()[1]):
            print()
        for i in range(self.size()):
            for k in range(self.position()[0]):
                    print(" ", end="")
            for j in range(self.size()):
                print("#", end="")
            print()

    @property
    def position(self):
        return self.__position

    @size.setter
    def position(self, position):
        if (not isinstance(position()[0], int))\
            or (not isinstance(position()[0], int))\
            or (position()[0] < 0) or (position()[1] < 0):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
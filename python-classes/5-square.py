#!/usr/bin/python3

"""
A class that defines any square
"""


class Square:

    """
    Square class with a positive integer size
    and area available. Size getter and setter included.
    The square can be printed.
    """

    def __init__(self, size=0):
        self.__size = size(size)

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
        for i in range(self.size()):
            for j in range(self.size()):
                print("#", end="")
            print()

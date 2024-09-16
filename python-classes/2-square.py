#!/usr/bin/python3

"""
A class that defines any square
"""


class Square:

    """
    Square class with a positive integer size
    """

    def __init__(self, size=0):
        if size < 0:
            raise TypeError("size must be an integer")
        if not isinstance(size, int):
            raise ValueError("size must be >= 0")
        self.__size = size

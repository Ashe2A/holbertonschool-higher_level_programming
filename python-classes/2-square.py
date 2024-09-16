#!/usr/bin/python3

"""
A class that defines any square
"""


class Square:

    """
    Square class with a size
    """

    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
            if size is not int:
                raise TypeError("size must be an integer")
        except (TypeError, ValueError) as e:
            print(e)

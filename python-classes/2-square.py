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
            if size < 0:
                raise ValueError("size must be >= 0")
            if size is not int:
                raise TypeError("size must be an integer")
            self.__size = size
        except (TypeError, ValueError) as e:
            print(e)

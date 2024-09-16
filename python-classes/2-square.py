#!/usr/bin/python3

"""
A class that defines any square
"""


class Square:

    """
    Square class with a positive integer size
    """

    def __init__(self, size=0):
        try:
            self.__size = size
        except (TypeError, ValueError) as e:
            print(e)

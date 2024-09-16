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
        except ValueError:
            if self.__size < 0:
                print("size must be >= 0")
        except TypeError:
            print("size must be an integer")

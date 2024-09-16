#!/usr/bin/python3

"""
A class that defines any square
"""


class Square:

    """
    Square class with a size
    """

    size = 0

    def __init__(self, __new_size):
        self.is_new = True
        if __new_size is not None:
            self.size = __new_size

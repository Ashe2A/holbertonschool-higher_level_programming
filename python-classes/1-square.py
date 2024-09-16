#!/usr/bin/python3

"""
A class that defines any square
"""


class Square:

    """
    Square class with a size
    """

    __size = 0

    def __init__(self, new_size):
        self.is_new = True
        if new_size is not None:
            self.size = new_size

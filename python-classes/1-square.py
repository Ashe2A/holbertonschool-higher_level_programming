#!/usr/bin/python3

"""
A class that defines any square
"""


class Square:

    """
    Square class with a size
    """

    _size = 0

    def __init__(self, _Square__size):
        if _Square__size is not None:
            self._size = _Square__size

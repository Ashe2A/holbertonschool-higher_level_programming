#!/usr/bin/python3
"""
Square.
"""


class Square:
    """
    Square class.
    """

    def __init__(self, size=0):
        """Square constructor

        Args:
            size (int): the size of the square
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Area of the square

        Returns:
            int: square of the size (area)
        """
        return self.__size ** 2

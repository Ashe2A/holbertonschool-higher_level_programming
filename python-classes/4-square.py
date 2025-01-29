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
        self.__size = size

    def area(self):
        """Area of the square

        Returns:
            int: square of the size (area)
        """
        return self.__size ** 2

    @property
    def size(self):
        """Square size getter

        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Square size setter

        Args:
            value (int): the new size

        Raises:
            ValueError: if negative size
            TypeError: if size is not a number
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

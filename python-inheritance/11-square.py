#!/usr/bin/python3

"""
A class that defines any square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square inherits Rectangle
    with an area method
    """

    def __init__(self, size):
        """
        Initialize Square.
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Area of the square.
        """

        return self.__size ** 2

    def __str__(self):
        """
        Square data.
        """
        return "[{}] {}/{}".format(str(self.__class__.__name__),
                                   self.__size, self.__size)
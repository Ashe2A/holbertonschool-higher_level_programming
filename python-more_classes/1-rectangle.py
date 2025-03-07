#!/usr/bin/python3
"""
Rectangle.
"""


class Rectangle:
    """
    Rectangle class.
    """

    def __init__(self, width=0, height=0):
        """Rectangle constructor

        Args:
            width (int, optional): Width of rectangle. Defaults to 0.
            height (int, optional): Height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter

        Returns:
            int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter

        Args:
            value (int): Width of the rectangle

        Raises:
            ValueError: If width is negative
            TypeError: If width is not integer
        """
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Height getter

        Returns:
            int: Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter

        Args:
            value (int): Height of the rectangle

        Raises:
            ValueError: If height is negative
            TypeError: If height is not integer
        """
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

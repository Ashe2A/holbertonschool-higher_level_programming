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

    def area(self):
        """Area of rectangle

        Returns:
            int: the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Perimeter of rectangle

        Returns:
            int: the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        """String representation of the rectangle.

        Returns:
            str: rectangle as a string
        """
        res = ""
        if not (self.__width == 0 or self.__height == 0):
            for i in range(self.__height):
                for j in range(self.__width):
                    res += "#"
                if i < self.__height - 1:
                    res += "\n"
        return res

    def __repr__(self):
        """Representation of class call

        Returns:
            str: Rectangle(<width>, <height>)
        """
        return "{}({}, {})".format(Rectangle.__name__,
                                   self.__width, self.__height)

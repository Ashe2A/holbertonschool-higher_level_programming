#!/usr/bin/python3

"""
A class that defines any rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle inherits BaseGeometry
    with an area method
    Printable.
    """

    def __init__(self, width, height):
        """
        Initialize Rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Area of the rectangle.
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Rectangle data.
        """
        return "[{}] {}/{}".format(str(self.__class__.__name__), self.__width, self.__height)

    def print(self):
        """
        Print the rectangle data.
        """
        print(str(self))

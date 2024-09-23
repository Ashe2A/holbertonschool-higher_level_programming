#!/usr/bin/python3

"""
A class that defines any rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle inherits BaseGeometry
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
        return self.__width * self.__height

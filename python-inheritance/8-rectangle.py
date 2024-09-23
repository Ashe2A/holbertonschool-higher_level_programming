#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
A class that defines any rectangle
"""


class Rectangle(BaseGeometry):

    """
    Rectangle inherits BaseGeometry
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

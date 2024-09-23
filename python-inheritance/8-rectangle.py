#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
A class that defines any rectangle
"""


class Rectangle(BaseGeometry):

    """
    Rectangle inherits BaseGeometry
    """

    def __init__(self, width=0, height=0):

        self.__width = super().integer_validator(self, "width", width)
        self.__height = super().integer_validator(self, "height", height)

    def area(self):
        return self.__width * self.__height

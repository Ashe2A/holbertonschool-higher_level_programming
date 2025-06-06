#!/usr/bin/python3
"""Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle subclass"""

    def __init__(self, width, height):
        """Rectangle constructor

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

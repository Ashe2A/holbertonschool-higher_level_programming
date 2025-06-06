#!/usr/bin/python3
"""Full Rectangle"""
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

    def area(self):
        """Area of the rectangle

        Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """String representation format

        Returns:
            str: string representation of the rectangle
        """
        return "[{}] {}/{}".format(__class__.__name__,
                                   self.__width, self.__height)

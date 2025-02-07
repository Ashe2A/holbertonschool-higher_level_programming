#!/usr/bin/python3
"""
Rectangle module.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class.
    """
    def __init__(self, width, height):
        if width is None:
            raise AttributeError("\'{}\' object has no attribute\
                 'width'".format(__name__))
        if height is None:
            raise AttributeError("\'{}\' object has no attribute\
                 'height'".format(__name__))
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

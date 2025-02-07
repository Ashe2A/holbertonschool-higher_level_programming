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
        """Rectangle constructor

        Args:
            width (int): width of the Rectangle
            height (height): height of the Rectangle

        Raises:
            AttributeError: if missing width arg
            AttributeError: if missing height arg
        """
        if width is None:
            raise AttributeError("\'{}\' object has no attribute\
                 'width'".format(__class__.__name__))
        if height is None:
            raise AttributeError("\'{}\' object has no attribute\
                 'height'".format(__class__.__name__))
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area of the Rectangle

        Returns:
            int: width times height
        """
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {}/{}".format(__class__.__name__, self.__width, self.__height)

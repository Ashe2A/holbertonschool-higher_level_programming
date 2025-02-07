#!/usr/bin/python3
"""
Base geometry module.
"""


class BaseGeometry():
    """
    Basic geometry interface.
    """

    def area(self):
        """Area of the figure

        Raises:
            Exception: not implemented
        """
        raise Exception("area() is not implemented")

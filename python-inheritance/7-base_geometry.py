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

    def integer_validator(self, name, value):
        """Validates an integer value

        Args:
            name (string): the name of the integer
            value (any): the potential integer

        Raises:
            TypeError: If value isn't an integer
            ValueError: If value is negative
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

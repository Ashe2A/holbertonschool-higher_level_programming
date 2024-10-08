#!/usr/bin/python3
"""
A class that defines any geometric object
"""


class BaseGeometry:
    """
    Improved geometry class
    with an abstract area
    and an integer value validator
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value

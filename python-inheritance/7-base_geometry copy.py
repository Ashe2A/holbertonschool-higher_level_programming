#!/usr/bin/python3

"""
A class that defines any geometric object with an abstract area
"""


class BaseGeometry:

    """
    Improved geometry class
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(int, value):
            raise TypeError("{} must be an integer".format(name))
        if not isinstance(int, value):
            raise ValueError("{} must be greater than 0".format(name))

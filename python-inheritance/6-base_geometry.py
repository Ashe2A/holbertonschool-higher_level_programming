#!/usr/bin/python3

"""
A class that defines any geometric object
"""


class BaseGeometry:

    """
    Improved geometry class
    with an abstract area
    """

    def area(self):
        raise Exception("area() is not implemented")

#!/usr/bin/python3

"""
A class that defines any geometric object with an abstract area
"""


class BaseGeometry:

    """
    Improved geometry class
    """

    def area(self):
        raise NotImplementedError()

#!/usr/bin/python3
"""
Abstract Shape Class and its Subclasses.
"""
from abc import ABC, abstractmethod
from math import pi
from typing import override


class Shape(ABC):
    """Shape abstract class

    Args:
        ABC (abc): abstract class module
    """

    @abstractmethod
    def area(self):
        """
        Abstract area method
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract perimeter method
        """
        pass


class Circle(Shape):
    """Circle class

    Args:
        Shape (Shape): A circle is a shape
    """

    def __init__(self, radius):
        """Circle constructor

        Args:
            radius (int, optional): radius of the circle. Defaults to 0.

        Raises:
            TypeError: if the radius isn't an integer
            ValueError: if the radius is negative
        """
        if not isinstance(radius, int):
            raise TypeError("Radius must be an integer")
        elif radius < 0:
            raise ValueError("Radius must be positive")
        else:
            self.radius = radius

    def area(self):
        """Circle area method

        Returns:
            int: Circle's area (pi x square of radius)
        """
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Circle circumference (perimeter)

        Returns:
            int: circumference of the Circle (2pi x radius)
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class

    Args:
        Shape (Shape): A rectangle is a shape
    """

    def __init__(self, width, height):
        """Rectangle constructor

        Args:
            width (int, optional): width of the Rectangle. Defaults to 0.
            height (int, optional): height of the Rectangle. Defaults to 0.

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is negative
            TypeError: if height is not an integer
            ValueError: if height is negative
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be positive")
        else:
            self.width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be positive")
        else:
            self.height = height

    def area(self):
        """Area of Rectangle

        Returns:
            int: area of rectangle (width x height)
        """
        return self.width * self.height

    def perimeter(self):
        """Perimeter of Rectangle

        Returns:
            int: perimeter of Rectangle
            (width x 2 + height x 2)
            or 0 if one of the dimensions is zero
        """
        if self.width != 0 and self.height != 0:
            2 * (self.width + self.height)
        else:
            return 0


def shape_info(shape):
    """Shape info printing
    Ducktyping allows dynamic methods between subclasses of the same class

    Args:
        shape (Shape): Any of the shapes called
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

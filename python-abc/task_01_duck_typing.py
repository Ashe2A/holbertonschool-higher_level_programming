#!/usr/bin/env python3
"""
Shape classes
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Shape abstract class
    """

    @abstractmethod
    def area(self):
        """
        Shape's area
        """

        pass

    @abstractmethod
    def perimeter(self):
        """
        Shape's perimeter
        """

        pass


class Circle(Shape):
    """
    Circle class
    """

    pi = math.pi

    def __init__(self, radius=0):
        if not isinstance(radius, int):
            raise TypeError("Radius must be an integer")
        if radius < 0:
            raise ValueError("Radius must be positive or zero")
        self.radius = radius

    def area(self):
        """
        Circle's area

        Parameters:
            self: the Circle

        Returns:
            Area of the Circle
        """

        return Circle.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Circle's circumference

        Parameters:
            self: the Circle

        Returns:
            Circumference of the Circle
        """

        return 2 * Circle.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        if (not isinstance(width, int)) or (not isinstance(height, int)):
            raise TypeError("Dimensions must be integers")
        if (height < 0) or (width < 0):
            raise ValueError("Dimensions must be positive or zero")
        self.width = width
        self.height = height

    def area(self):
        """
        Rectangle's area

        Parameters:
            self: the Rectangle

        Returns:
            Area of the Rectangle
        """

        return self.width * self.height

    def perimeter(self):
        """
        Rectangle's perimeter

        Parameters:
            self: the Rectangle

        Returns:
            Perimeter of the Rectangle
        """

        if (self.width == 0) or (self.height == 0):
            return 0
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Displays infos on the Shape

    Parameters:
        shape: the shape
    """

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

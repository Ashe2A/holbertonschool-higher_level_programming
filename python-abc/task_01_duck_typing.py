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

    def __init__(self, radius):
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

        return abs(2 * Circle.pi * self.radius)


class Rectangle(Shape):
    """
    Rectangle class
    """

    def __init__(self, width, height):
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

        return abs(2 * (self.width + self.height))


def shape_info(shape):
    """
    Displays infos on the Shape

    Parameters:
        shape: the shape
    """

    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

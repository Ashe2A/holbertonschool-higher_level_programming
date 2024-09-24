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

        raise Exception("area() is not implemented")

    @abstractmethod
    def perimeter(self):
        """
        Shape's perimeter
        """

        raise Exception("perimeter() is not implemented")


class Circle(Shape):
    """
    Circle class
    """

    pi = math.pi

    def __init__(self, radius=0):
        self.__radius = radius

    def area(self):
        """
        Circle's area

        Parameters:
            self: the Circle

        Returns:
            Area of the Circle
        """

        return Circle.pi * (self.__radius ** 2)

    def perimeter(self):
        """
        Circle's circumference

        Parameters:
            self: the Circle

        Returns:
            Circumference of the Circle
        """

        return 2 * Circle.pi * self.__radius


class Rectangle(Shape):
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def area(self):
        """
        Rectangle's area

        Parameters:
            self: the Rectangle

        Returns:
            Area of the Rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Rectangle's perimeter

        Parameters:
            self: the Rectangle

        Returns:
            Perimeter of the Rectangle
        """

        return 2 * (self.__width + self.__height)

def shape_info(shape):
    """
    Displays infos on the Shape

    Parameters:
        shape: the shape
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
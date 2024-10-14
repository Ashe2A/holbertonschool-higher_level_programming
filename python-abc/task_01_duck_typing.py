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
        elif radius < 0:
            raise ValueError("Radius must be positive or zero")
        else:
            self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        if not isinstance(radius, int):
            raise TypeError("Radius must be an integer")
        elif radius < 0:
            raise ValueError("Radius must be positive or zero")
        else:
            self.__radius= radius

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
        if (not isinstance(width, int)):
            raise TypeError("Width must be integers")
        elif (not isinstance(height, int)):
            raise TypeError("Height must be integers")
        elif (width < 0):
            raise ValueError("Width must be positive or zero")
        elif (height < 0):
            raise ValueError("Height must be positive or zero")
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")
        elif width < 0:
            raise ValueError("Width must be positive or zero")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("Height must be integers")
        elif height < 0:
            raise ValueError("Height must be positive or zero")
        else:
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

        if (self.__width == 0) or (self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Displays infos on the Shape

    Parameters:
        shape: the shape
    """

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

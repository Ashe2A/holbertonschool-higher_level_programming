#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
"""
Duck typing with shapes
"""

class Shape(ABC):
    """Shape class

    Inherits:
        ABC (class): abstract class
    """

    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class

    Inherits:
        Shape (class): Basic shape class
    """

    def __init__(self, radius):
        """Circle constructor

        Args:
            radius (int): radius of the circle
        """
        self.radius = radius

    def area(self):
        """Area of the circle

        Returns:
            int: area of the circle (pi x square of radius)
        """
        return pi * (self.radius ** 2)
    
    def perimeter(self):
        """Perimeter of the circle

        Returns:
            int: perimeter of the circle (2 x pi x radius)
        """
        return 2 * pi * self.radius

class Rectangle(Shape):
    """Rectangle class

    Args:
        Shape (class): Basic shape class
    """
    def __init__(self, height, width):
        """Rectangle constructor

        Args:
            height (int): height of the circle
            width (int): width of the circle
        """
        self.height = height
        self.width = width

    def area(self):
        """Area of the rectangle

        Returns:
            int: area of the rectangle (height x width)
        """
        return self.height * self.width

    def perimeter(self):
        """Perimeter of the rectangle

        Returns:
            int: perimeter of the rectangle (height x 2 + width x 2)
        """
        return 0 if self.height == 0 or self.width == 0 \
            else self.height * 2 + self.width * 2

#!/usr/bin/python3
'''Shapes, Interfaces, and Duck Typing'''
from abc import ABC
from abc import abstractmethod
from math import pi


class Shape(ABC):
    '''Shape abstract class

    Args:
        ABC (class): Inherits from abstract class
    '''

    @abstractmethod
    def area(self):
        '''Area abstract class'''
        pass

    @abstractmethod
    def perimeter(self):
        '''Perimeter abstract class'''
        pass


class Circle(Shape):
    '''Circle subclass of Shape

    Args:
        Shape (abstractclass): Inherits from Shape superclass
    '''

    def __init__(self, radius=0):
        '''Circle constructor

        Args:
            radius (int, optional): Radius of the circle. Defaults to 0.
        '''
        self.radius = radius

    def area(self):
        '''Area of the circle

        Returns:
            int: area of the circle (pi·r²)
        '''
        return (self.radius ** 2) * pi

    def perimeter(self):
        '''Circumference of the circle

        Returns:
            int: circumference of the circle (pi·2r)
        '''
        return self.radius * pi * 2


class Rectangle(Shape):
    '''Rectangle subclass of Shape

    Args:
        Shape (abstractclass): Inherits from Shape superclass
    '''

    def __init__(self, width=0, height=0):
        '''Rectangle constructor

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        '''
        self.width = width
        self.height = height

    def area(self):
        '''Area of the rectangle

        Returns:
            int: area of the rectangle (wh)
        '''
        return self.width * self.height

    def perimeter(self):
        '''Perimeter of the rectangle

        Returns:
            int: perimeter of the rectangle (2(w+h))
        '''
        if self.width <= 0 or self.height <= 0:
            return 0
        return 2 * (self.width + self.height)


def shape_info(shape):
    '''Display shape info

    Args:
        shape (Shape): shape object
            (must be subclass of Shape abstract class)
    '''
    print('Area: {}'.format(shape.area()))
    print('Perimeter: {}'.format(shape.perimeter()))

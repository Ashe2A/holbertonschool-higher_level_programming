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

    def __init__(self, radius):
        '''Circle constructor

        Args:
            radius (int): Radius of the circle.
        '''
        self.__radius = radius

    def area(self):
        '''Area of the circle

        Returns:
            int: area of the circle (pi·r²)
        '''
        return (self.__radius ** 2) * pi

    def perimeter(self):
        '''Circumference of the circle

        Returns:
            int: circumference of the circle (pi·2r)
        '''
        return abs(self.__radius * pi * 2)


class Rectangle(Shape):
    '''Rectangle subclass of Shape

    Args:
        Shape (abstractclass): Inherits from Shape superclass
    '''

    def __init__(self, width, height):
        '''Rectangle constructor

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        '''
        self.__width = width
        self.__height = height

    def area(self):
        '''Area of the rectangle

        Returns:
            int: area of the rectangle (wh)
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''Perimeter of the rectangle

        Returns:
            int: perimeter of the rectangle (2(w+h))
        '''
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    '''Display shape info

    Args:
        shape (Shape): shape object
            (must be subclass of Shape abstract class)
    '''
    print('Area: {}'.format(shape.area()))
    print('Perimeter: {}'.format(shape.perimeter()))

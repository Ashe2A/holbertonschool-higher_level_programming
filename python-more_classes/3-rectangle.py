#!/usr/bin/python3
'''Real definition of a rectangle'''


class Rectangle():
    '''Rectangle class'''

    def __init__(self, width=0, height=0):
        '''Rectangle constructor

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Width getter

        Returns:
            int: the width of the rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Width setter

        Args:
            value (int): The value to set the width with

        Raises:
            TypeError: If the value isn't an integer
            ValueError: If the value is a negative integer
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Height getter

        Returns:
            int: the height of the rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Height setter

        Args:
            value (int): The value to set the height with

        Raises:
            TypeError: If the value isn't an integer
            ValueError: If the value is a negative integer
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''Area of the rectangle

        Returns:
            int: area of the rectangle (height x width)
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''Perimeter of the rectangle

        Returns:
            int: perimeter of the rectangle (2 * height + 2 * width)
        '''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        '''String representation of rectangle

        Returns:
            str: string representation of rectangle
        '''
        res = ''
        for i in range(self.__height):
            for j in range(self.__width):
                res += '#'
            res += '\n'
        return res

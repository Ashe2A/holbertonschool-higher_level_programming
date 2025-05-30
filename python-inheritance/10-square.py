#!/usr/bin/python3
'''Square #1'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square subclass'''

    def __init__(self, size):
        '''Square constructor

        Args:
            size (int): size of the square
        '''
        self.__size = self.integer_validator('size', size)

    def area(self):
        '''Area of the square

        Returns:
            int: the area of the square
        '''
        return self.__size ** 2

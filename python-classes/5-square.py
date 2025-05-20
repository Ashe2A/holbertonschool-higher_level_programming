#!/usr/bin/python3
'''Printing a square'''


class Square():
    '''Square class'''

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        '''Area of the square

        Returns:
            int: area of the square
        '''
        return self.__size ** 2

    @property
    def size(self):
        '''Size getter

        Returns:
            int: size of the square
        '''
        return self.__size

    @size.setter
    def size(self, size):
        '''Size setter

        Args:
            size (int): the size of the square

        Raises:
            TypeError: If size isn't int
            ValueError: If size is negative
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

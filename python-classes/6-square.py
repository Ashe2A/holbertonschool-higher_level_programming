#!/usr/bin/python3
"""
Square.
"""


class Square:
    """
    Square class.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Square constructor

        Args:
            size (int): the size of the square
            position (tuple of int): the position of the square
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Area of the square

        Returns:
            int: square of the size (area)
        """
        return self.__size ** 2

    def my_print(self):
        """
        print the square with #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """Square size getter

        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Square size setter

        Args:
            value (int): the new size

        Raises:
            ValueError: if negative size
            TypeError: if size is not a number
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Square position getter

        Returns:
            tuple of int: the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Square position setter

        Args:
            value (tuple of int): The new position of the square
        """
        if isinstance(value, tuple) and \
            len(value) == 2 and \
                isinstance(value[0], int) and \
                isinstance(value[1], int) and \
                value[0] >= 0 or value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

#!/usr/bin/python3
"""Coordinates of a square"""


class Square():
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize instance attributes

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): Position of the square.
                Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size getter

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter

        Args:
            size (int): the size of the square

        Raises:
            TypeError: If size isn't int
            ValueError: If size is negative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position getter

        Returns:
            tuple of int: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter

        Args:
            value (tuple of int): the position of the square

        Raises:
            TypeError: If the position isn't a tuple of positive int
        """
        if not (isinstance(value, tuple) and len(value) == 2
                and isinstance(value[0], int) and isinstance(value[1], int)
                and value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of the square

        Returns:
            int: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print square depending on size

        Returns:
            Absolutely nothing.
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

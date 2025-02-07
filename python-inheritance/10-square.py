#!/usr/bin/python3
"""
Square module.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle.
    """
    def __init__(self, size):
        """Square constructor

        Args:
            size (int): size of the Square

        Raises:
            AttributeError: if missing size arg
        """
        if size is None:
            raise AttributeError("\'{}\' object has no attribute\
                 'size'".format(__class__.__name__))
        self.__size = self.integer_validator("size", size)

    def area(self):
        """Area of the Square

        Returns:
            int: square of the size
        """
        return self.__size ** 2

    def __str__(self):
        return "[{}] {}/{}".format(__class__.__bases__[0].__name__,
                                   self.__size, self.__size)

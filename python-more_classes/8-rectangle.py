#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle():
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Rectangle constructor

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        __class__.number_of_instances += 1

    @property
    def width(self):
        """Width getter

        Returns:
            int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter

        Args:
            value (int): The value to set the width with

        Raises:
            TypeError: If the value isn't an integer
            ValueError: If the value is a negative integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter

        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter

        Args:
            value (int): The value to set the height with

        Raises:
            TypeError: If the value isn't an integer
            ValueError: If the value is a negative integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle

        Returns:
            int: area of the rectangle (height x width)
        """
        return self.__height * self.__width

    def perimeter(self):
        """Perimeter of the rectangle

        Returns:
            int: perimeter of the rectangle (2 * height + 2 * width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """String representation of rectangle

        Returns:
            str: string representation of rectangle
        """
        res = ""
        if self.__height > 0 and self.__width > 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    res += "{}".format(self.print_symbol)
                if i < self.__height - 1:
                    res += "\n"
        return res

    def print(self):
        """Print the rectangle"""
        print(self.__str__, end="")

    def __repr__(self):
        """Representation of Rectangle object

        Returns:
            str: The string representation of the rectangle
        """
        return "{}({}, {})".format(__class__.__name__,
                                   self.__width, self.__height)

    def __del__(self):
        """Print goodbye (and pray your god)"""
        __class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Biggest or equal rectangle

        Args:
            rect_1 (Rectangle): the first rectangle
            rect_2 (Rectangle): the second rectangle

        Raises:
            TypeError: If the first rectangle isn't a Rectangle
            TypeError: If the second rectangle isn't a Rectangle

        Returns:
            Rectangle: the biggest of both rectangle,
                or the first one if they're as large
        """
        if not isinstance(rect_1, __class__):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, __class__):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

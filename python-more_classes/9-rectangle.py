#!/usr/bin/python3
"""
Rectangle.
"""


class Rectangle:
    """
    Rectangle class.
    """

    number_of_instances = 0  # Number of rectangles constructed
    print_symbol = "#"  # String representation char

    def __init__(self, width=0, height=0):
        """Rectangle constructor

        Args:
            width (int, optional): Width of rectangle. Defaults to 0.
            height (int, optional): Height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width getter

        Returns:
            int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter

        Args:
            value (int): Width of the rectangle

        Raises:
            ValueError: If width is negative
            TypeError: If width is not integer
        """
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Height getter

        Returns:
            int: Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter

        Args:
            value (int): Height of the rectangle

        Raises:
            ValueError: If height is negative
            TypeError: If height is not integer
        """
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Area of rectangle

        Returns:
            int: the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Perimeter of rectangle

        Returns:
            int: the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        """String representation of the rectangle.

        Returns:
            str: rectangle as a string
        """
        res = ""
        if not (self.__width == 0 or self.__height == 0):
            for i in range(self.__height):
                for j in range(self.__width):
                    res += "{}".format(getattr(self, 'print_symbol',
                                               Rectangle.print_symbol))
                if i < self.__height - 1:
                    res += "\n"
        return res

    def __repr__(self):
        """Representation of class call

        Returns:
            str: Rectangle(<width>, <height>)
        """
        return "{}({}, {})".format(Rectangle.__name__,
                                   self.__width, self.__height)

    def __del__(self):
        """When you delete the rectangle, what happens?
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Bigger or equal

        Args:
            rect_1 (Rectangle): first Rectangle
            rect_2 (Rectangle): second Rectangle

        Raises:
            TypeError: if rect_1 isn't a Rectangle
            TypeError: if rect_2 isn't a Rectangle

        Returns:
            Rectangle: the biggest rectangle, or rect_1 if equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Square as a Rectangle

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Returns:
            Rectangle: a Rectangle with equal width and height
        """
        return Rectangle(size, size)

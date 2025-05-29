#!/usr/bin/python3
'''Integer validator'''


class BaseGeometry():
    '''Base geometry class'''

    def area(self):
        '''Area of the base geometrical figure

        Raises:
            Exception: if area is not implemented in subclasses
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Integer validator for attributes

        Args:
            name (str): The name of the integer. Must always be string.
            value (int): Value of the integer.

        Raises:
            TypeError: If value isn't an integer
            ValueError: If value is 0 or under
        '''
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        return value

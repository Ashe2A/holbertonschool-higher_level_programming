#!/usr/bin/python3
'''Improve Geometry'''


class BaseGeometry():
    '''Base geometry class'''

    def area(self):
        '''Area of the base geometrical figure

        Raises:
            Exception: if area is not implemented in subclasses
        '''
        raise Exception('area() is not implemented')

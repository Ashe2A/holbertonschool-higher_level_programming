#!/usr/bin/python3
'''Exact same object'''

def is_same_class(obj, a_class):
    '''Checks if object is from the same class

    Args:
        obj (obj): The object to identify
        a_class (class): The class to check

    Returns:
        bool: True if obj is a_class, False otherwise
    '''
    return obj is a_class

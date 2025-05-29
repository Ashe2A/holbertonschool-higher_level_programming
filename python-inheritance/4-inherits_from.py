#!/usr/bin/python3
'''Only sub class of'''


def inherits_from(obj, a_class):
    '''Checks if object is an instance of subclass

    Args:
        obj (obj): The object to identify
        a_class (class): The superclass to check

    Returns:
        bool: True if obj is a subclass instance of a_class, False otherwise
    '''
    return isinstance(obj, a_class) and not type(obj) is a_class

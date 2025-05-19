#!/usr/bin/python3
def safe_print_integer(value):
    '''Prints an integer and checking it's an integer

    Args:
        value (int): The integer, should be an integer or else...

    Returns:
        bool: True if printed, False if not (not an integer)
    '''
    try:
        print('{:d}'.format(value))
        return True
    except (TypeError, ValueError):
        return False

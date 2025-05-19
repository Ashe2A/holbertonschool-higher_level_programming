#!/usr/bin/python3
def safe_print_division(a, b):
    '''Divides and prints division

    Args:
        a (int): divided
        b (int): divisor

    Returns:
        float: Result of division
    '''
    res = 0.0
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print('Inside result: {}'.format(res))
        return res

#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Integer division's safe printing.
    """

    try:
        res = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res

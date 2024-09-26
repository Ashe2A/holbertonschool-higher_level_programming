#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Integer division's safe printing.
    """

    try:
        print("Inside result: {}".format(a / b))
        return a / b
    except (TypeError, ValueError, ZeroDivisionError):
        pass
    finally:
        print("Inside result: None")
    return None

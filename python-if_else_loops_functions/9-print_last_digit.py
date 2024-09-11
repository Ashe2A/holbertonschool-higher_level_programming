#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints the last digit of a number.

    Parameters:
        number (int): number to print the last digit of.

    Returns:
        The last digit of number.
    """
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit

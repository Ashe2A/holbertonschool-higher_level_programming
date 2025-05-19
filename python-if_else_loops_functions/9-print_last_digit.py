#!/usr/bin/python3
def print_last_digit(number):
    '''Prints last digit of a number

    Args:
        number (int): The number

    Returns:
        int: Last digit of the number
    '''
    last_digit = abs(number) % 10
    print('{}'.format(last_digit), end='')
    return last_digit

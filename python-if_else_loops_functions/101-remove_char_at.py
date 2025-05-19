#!/usr/bin/python3
def remove_char_at(str, n):
    '''Remove a character from the string

    Args:
        str (str): The string
        n (int): The index to pop

    Returns:
        str: A new string minus the indicated character
    '''
    if n >= 0:
        return str[0:n] + str[(n + 1):len(str)]
    else:
        return str

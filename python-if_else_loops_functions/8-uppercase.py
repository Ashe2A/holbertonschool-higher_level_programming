#!/usr/bin/python3
def uppercase(str):
    """
    Uppercase a string.

    Parameters:
        str (str): String to upper.
    """
    for i in range(len(str)):
        if ord('a') <= ord(str[i]) <= ord('z'):
            print(chr(ord(str[i]) + ord('A') - ord('a')), end="")
        else:
            print(str[i], end="")
    print("")
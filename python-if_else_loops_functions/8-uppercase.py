#!/usr/bin/python3
def uppercase(str):
    """
    Uppercase a string.

    Parameters:
        str (str): String to upper.
    """
    for i in range(len(str)):
        print("{}".format(chr(ord(str[i]) + ord('A') - ord('a')))
             if ord('a') <= ord(str[i]) <= ord('z') else "{}".format(str[i]), end="")
    print()

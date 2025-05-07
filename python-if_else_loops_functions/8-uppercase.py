#!/usr/bin/python3
def uppercase(str):
    """Prints string converted into uppercase

    Args:
        str (str): String
    """
    for i in str:
        if ord("a") <= ord(i) <= ord("z"):
            i = chr(ord(i) + ord("A") - ord("a"))
        print("{}".format(i), end="")
    print()

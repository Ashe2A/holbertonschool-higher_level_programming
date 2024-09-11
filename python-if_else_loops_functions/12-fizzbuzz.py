#!/usr/bin/python3
def fizzbuzz():
    """
    Prints fizzbuzz.
    """
    for i in range(100):
        if ((i + 1) % 3) == 0:
            print("Fizz", end="")
        if ((i + 1) % 5) == 0:
            print("Buzz", end="")
        if not (((i + 1) % 3) == 0) and not (((i + 1) % 5) == 0):
            print("{}".format(i + 1), end="")
        print("", end=" ")

#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) - 1 >= 0:
        argument = "argument"
        if len(argv) - 1 != 1:
            argument += "s"
        if len(argv) - 1 == 0:
            argument += "."
        else:
            argument += ":"
        print("{} {}".format(len(argv) - 1, argument))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))

#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    print("{} argument".format(len(argv)), end="")
    if len(argv) == 1:
        print("s.")
    elif len(argv) == 2:
        print(":")
    else:
        print("s:")
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))

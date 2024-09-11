#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    res = 0
    for i in range(1, len(argv)):
        res += int(argv[i])
    print("{}".format(res))

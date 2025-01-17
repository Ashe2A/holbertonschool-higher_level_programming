#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1
    argcstr = f"{argc} argument"
    if argc != 1:
        argcstr += "s"
    if argc == 0:
        argcstr += "."
    else:
        argcstr += ":"
    print(f"{argcstr}")
    for i in range(argc):
        print(f"{i + 1}: {argv[i + 1]}")

#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if not ((i == ord('e')) or (i == ord('q'))):
        print("{}".format(chr(i)), end="")

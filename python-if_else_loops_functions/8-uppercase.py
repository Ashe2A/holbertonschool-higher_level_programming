#!/usr/bin/python3

def uppercase(str):
    for i in str:
        print("{}".format(chr(ord(i) + ord('A') - ord('a')))
              if ord('a') <= ord(i) <= ord('z')
              else "{}".format(i), end="")
    print()

#!/usr/bin/python3

def uppercase(str):
    for i in str:
        print(chr(ord(i) + ord('A') - ord('a'))
              if ord('a') <= ord(i) <= ord('z')
              else i, end="")
    print()

#!/usr/bin/python3
import dis
from calculator_1 import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    elif a > b:
        return sub(a, b)


dis.dis(magic_calculation)

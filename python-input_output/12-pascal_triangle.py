#!/usr/bin/python3

"""
Pascal triangle.
"""

import json


def pascal_triangle(n):
    """
    Prints Pascal triangle.

    Parameters:
        n: size.
    """


    triangle = []
    for i in range(n):
        triangle.append([])
        for j in range(i):
            if 0 < j < i:
                triangle[i].append(triangle[i - 1][j - 1]
                                   + triangle[i - 1][j])
            else:
                triangle[i].append(1)
    print(triangle)

#!/usr/bin/python3
"""
Pascal triangle.
"""

def pascal_triangle(n):
    """
    Prints Pascal triangle.

    Parameters:
        n: size.
    """

    triangle = []
    if n > 0:
        for i in range(n):
            triangle.append([])
            for j in range(i):
                if 0 < j < i:
                    app = triangle[i - 1][j - 1] + triangle[i - 1][j]
                    triangle[i].append(app)
                else:
                    triangle[i].append(1)
    return triangle

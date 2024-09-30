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

    ptri = []
    if n > 0:
        for i in range(n):
            ptri.append([])
            for j in range(i + 1):
                if 0 < j < i:
                    app = ((ptri[i - 1])[j - 1]) + ((ptri[i - 1])[j])
                    ptri[i].append(app)
                else:
                    ptri[i].append(1)
    return ptri

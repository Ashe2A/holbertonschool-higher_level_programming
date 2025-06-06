#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Generating Pascal triangle

    Args:
        n (int): size of the triangle

    Returns:
        list: Pascal triangle
    """
    p_tri = []
    if n > 0:
        for i in range(n):
            p_tri_row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    p_tri_row.append(1)
                else:
                    p_tri_row.append(p_tri[i - 1][j] + p_tri[i - 1][j - 1])
            p_tri.append(p_tri_row)
    return p_tri

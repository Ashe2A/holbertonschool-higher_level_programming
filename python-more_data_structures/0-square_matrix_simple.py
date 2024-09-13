#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Square of matrix.

    Parameters:
        matrix : the original matrix

    Returns : the squared (or not) matrix
    """
    return list(map(lambda x: x**2, matrix))

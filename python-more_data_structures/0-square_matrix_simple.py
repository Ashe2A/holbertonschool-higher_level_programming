#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Square of matrix.

    Parameters:
        matrix : the original matrix

    Returns : the squared (or not) matrix
    """
    new_matrix = []
    for i in matrix:
        new_i = []
        for j in i:
            new_i.append(j * j)
        new_matrix.append(new_i)
    return new_matrix

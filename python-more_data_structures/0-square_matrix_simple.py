#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''Squares up a matrix

    Args:
        matrix (list, optional): The matrix. Defaults to empty list.

    Returns:
        list(list): The squared up matrix
    '''
    new_matrix = []
    for i in matrix:
        new_i = []
        for j in i:
            new_i.append(j ** 2)
        new_matrix.append(new_i)
    return new_matrix

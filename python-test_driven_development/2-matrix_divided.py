#!/usr/bin/python3
'''Divide a matrix'''


def matrix_divided(matrix, div=1):
    '''Divide a matrix by a number

    Args:
        matrix (list of list): The matrix
        div (int, optional): The number to divide the matrix with.
            Defaults to 1.

    Raises:
        TypeError: matrix is not a list of list of integers
        TypeError: uneven matrix
        TypeError: div isn't a number
        ZeroDivisionError: div is zero

    Returns:
        list of list: the new divided matrix
    '''
    if not (isinstance(matrix, list)
            and (all(isinstance(i, list)
                 and all(isinstance(j, (int, float)) for j in i)
                 for i in matrix))):
        raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    for i in matrix:
        new_row = []
        for j in i:
            if div == 1:
                new_row.append(j)
            else:
                new_row.append(round(j / div, 2))
        new_matrix.append(new_row)
    return new_matrix

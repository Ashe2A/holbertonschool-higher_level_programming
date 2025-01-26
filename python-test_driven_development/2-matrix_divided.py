#!/usr/bin/python3
"""
Divide matrix.
matrix_divided is the function to divide matrix
The matrix are made of integers
Usage: x = matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix by a number.

    Params:
        matrix: the integer matrix
        div: non zero number (float or integer)

    Return:
        A new matrix with the original's divided integers
    """
    new_matrix = []
    matrix_type_error = "matrix must be a matrix (list of lists)"
    matrix_type_error += " of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(matrix_type_error)
    else:
        for i in matrix:
            if not isinstance(i, list):
                raise TypeError(matrix_type_error)
            else:
                for j in i:
                    if not (isinstance(j, int) or isinstance(j, float)):
                        raise TypeError(matrix_type_error)

    matrix_first_row_len = len(matrix[0])
    for i in matrix:
        if len(i) != matrix_first_row_len:
            raise TypeError("Each row of the matrix must have the same size")

    div_number = "div must be a number"
    if not isinstance(div, (int, float)):
        raise TypeError(div_number)
    if div == float('NaN'):
        raise ValueError(div_number)
    if div == float('inf'):
        raise OverflowError(div_number)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        new_matrix.append([])
        for j in i:
            new_matrix[len(new_matrix) - 1].append(round((j / div), 2))
    return new_matrix

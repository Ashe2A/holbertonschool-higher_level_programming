#!/usr/bin/python3

""" Tests function to divide matrix integers with exceptions """


def matrix_divided(matrix, div):
    """ Divide matrix """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not (isinstance(matrix[i][j], (int, float))):
                raise TypeError("matrix must be a matrix (list of lists)\
                                of integers/floats")

    zerolen = len(matrix[0])
    for i in matrix:
        if len(i) != zerolen:
            raise TypeError("Each row of the matrix must have the same size")

    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(round(j / div, 2))

    return new_matrix
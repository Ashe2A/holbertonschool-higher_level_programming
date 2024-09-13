#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix.

    Parameters:
        matrix (list of list) : the matrix.
    """
    for i in matrix:
        for j in i:
            if j != i[len(i) - 1]:
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j))


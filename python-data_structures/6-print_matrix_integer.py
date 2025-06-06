#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print integer matrix

    Args:
        matrix (list of list): The matrix
    """
    for i in matrix:
        matrix_end = " "
        for j in i:
            if j == i[len(i) - 1]:
                matrix_end = "\n"
            print("{:d}".format(j), end=matrix_end)
    if matrix == [[]]:
        print()

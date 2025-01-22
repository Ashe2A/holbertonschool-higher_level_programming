#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    square_matrix = list(map(lambda i: list(map(lambda x: x * x, i)), matrix))
    return square_matrix

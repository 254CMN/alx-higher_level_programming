#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of integers in a matrix"""

    rows = len(matrix)
    col = len(matrix[0])
    for i in range(rows):
        for j in range(col):
            matrix[i][j] **= 2

    return matrix


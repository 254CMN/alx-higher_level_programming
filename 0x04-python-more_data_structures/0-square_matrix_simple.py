#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of integers in a matrix"""

    mod_matrix = []
    for row in matrix:
        squared_row = []
        for num in row:
            squared_row.append(num**2)
        mod_matrix.append(squared_row)
    return mod_matrix


#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = ([list(map(lambda x: x*x, m)) for m in matrix])
    return (new_matrix)

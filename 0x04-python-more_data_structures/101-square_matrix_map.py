#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    # Use nested 'map' functions to create a new matrix with elements squared.
    return list(map(lambda row: list(map(lambda col: col**2, row)), matrix))

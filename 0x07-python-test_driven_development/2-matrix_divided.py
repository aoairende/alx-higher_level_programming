#!/usr/bin/python3

""" Module defines a function that performs matrix division """


def matrix_divided(matrix, div):
    """ Divides all elements of matrix by div """

    # Validate the input matrix and divisor.

    # Check if 'matrix' is a list of lists containing integers or floats.
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        # Check if 'div' is a number (int or float) and not zero.
        for value in row:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and round the results to two decimal places.
    return [[round(value / div, 2) for value in row] for row in matrix]

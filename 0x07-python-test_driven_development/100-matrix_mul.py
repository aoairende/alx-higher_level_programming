#!/usr/bin/python3

"""
Module defines a function named "matrix_mul" that multiplies 
two matrices, "m_a" and "m_b".
"""


def matrix_mul(m_a, m_b):

    # Check if "m_a" is a list, and if not, raise a TypeError.
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    # Check if "m_b" is a list, and if not, raise a TypeError.
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Validate the elements in matrix m_a.
    for row in m_a:

        # Check if each row in m_a is a list, and if not, raise a TypeError.
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")

        """
        Check if each value in the row is either an integer or a float, 
        and if not, raise a TypeError.
        """
        for value in row:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("m_a should contain only integers or floats")

        """
        Check if each row has the same size as the first row in m_a, 
        indicating consistent column sizes.
        """
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    # Validate the elements in matrix m_b following the same logic as m_a.
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        for value in row:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("m_b should contain only integers or floats")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    # Check if m_a and m_b are not empty matrices.
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    # Calculate the dimensions of matrices m_a and m_b.
    num_rows_in_a = len(m_a)
    num_cols_in_a = len(m_a[0])
    num_rows_in_b = len(m_b)
    num_cols_in_b = len(m_b[0])

    """
    Check if the number of columns in m_a matches the number of rows 
    in m_b for matrix multiplication.
    """
    if num_cols_in_a != num_rows_in_b:
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize a result matrix with zeros.
    mul_result = [[0] * num_cols_in_b for _ in range(num_rows_in_a)]

    # Perform matrix multiplication.
    for i in range(num_rows_in_a):
        for j in range(num_cols_in_b):
            for k in range(num_cols_in_a):
                mul_result[i][j] += m_a[i][k] * m_b[k][j]

    # Return the resulting matrix after multiplication.
    return mul_result

#!/usr/bin/python3
""" Import the numpy library for matrix multiplication. """
import numpy

"""
Define a function named "lazy_matrix_mul" that performs 
matrix multiplication using numpy.
"""
def lazy_matrix_mul(m_a, m_b):

    """
    Use the numpy "matmul" function to multiply matrices "m_a" and "m_b" 
    and return the result.
    """
    return numpy.matmul(m_a, m_b)

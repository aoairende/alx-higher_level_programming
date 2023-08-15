#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    # Initialize variables to store the values from the tuples.
    arg1_a = 0
    arg1_b = 0
    arg2_a = 0
    arg2_b = 0

    # Check the length of tuple_a to determine how to assign values to the variables.
    if len(tuple_a) == 1:
        arg1_a = tuple_a[0]
    elif len(tuple_a) > 1:
        arg1_a = tuple_a[0]
        arg1_b = tuple_a[1]

    # Check the length of tuple_b to determine how to assign values to the variables.
    if len(tuple_b) == 1:
        arg2_a = tuple_b[0]
    elif len(tuple_b) > 1:
        arg2_a = tuple_b[0]
        arg2_b = tuple_b[1]

    return (arg1_a + arg2_a, arg1_b + arg2_b)

#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    # Initialize a variable to store the length of each row.
    row_len = 0
    if not matrix:
        print()

    # Iterate through each row in the matrix.
    for row in matrix:
        row_len = len(row)

        # Iterate through each element in the row.
        for idx, col in enumerate(row):
            if idx != row_len - 1:
                print("{:d}".format(col), end=" ")
            else:
                print("{:d}".format(col), end="")
        print()

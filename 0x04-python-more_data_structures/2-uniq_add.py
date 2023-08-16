#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0    # Initialize the sum variable to store the calculated sum.
    uniq = set(my_list)
    for x in uniq:    # Iterate over each unique element in the set
        # Add the current element to the sum.
        sum += x
    return sum

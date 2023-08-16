#!/usr/bin/python3

def weight_average(my_list=[]):
    # Check if the input list is empty.
    if not my_list:
        return 0
    # Initiate the sum of weights.
    weighted_score = 0
    weighted_total = 0

    # Iterate through each score-weight tuple in the list.
    for score, weight in my_list:
        weighted_score += score * weight
        weighted_total += weight
    return weighted_score / weighted_total

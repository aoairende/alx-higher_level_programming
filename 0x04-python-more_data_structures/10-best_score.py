#!/usr/bin/python3

def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # Initialize 'best_key' with the first key
    best_key = list(a_dictionary.keys())[0]
    # Initialize 'max_value' with the value of the first key
    max = a_dictionary[best_key]

    # Iterate through the dictionary to find the key with the highest value
    for key, value in a_dictionary.items():
        if value > max:
            max = value
            best_key = key
    return best_key

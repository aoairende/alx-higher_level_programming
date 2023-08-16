#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    # Initialize a flag to check if specified value exists in the dictionary
    exist = False

    # Check if the specified value exists in any of the dictionary's values
    for x in list(a_dictionary.values()):
        if x == value:
            exist = True

    # If the value doesn't exist, return the original dictionary
    if not exist:
        return a_dictionary
    pairs = list(a_dictionary.items())

    # Iterate through the list of key-value pairs and delete pairs
    # with the specified value.
    for key, val in pairs:
        if val == value:
            del a_dictionary[key]
    return a_dictionary

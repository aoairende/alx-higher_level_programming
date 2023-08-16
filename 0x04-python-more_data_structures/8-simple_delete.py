#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Check if the specified key exists in the dictionary
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

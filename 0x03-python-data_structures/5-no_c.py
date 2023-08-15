#!/usr/bin/python3

def no_c(my_string):

    # Initialize an empty string to store the filtered characters.
    no_c_str = ""

    # Iterate through each character in the input string.
    for ch in my_string:
        if ch != "c" and ch != "C": # Check if the character is not 'c' or 'C'.
            no_c_str += ch # Append the character to the filtered string.
    return no_c_str

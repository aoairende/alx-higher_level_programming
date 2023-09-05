#!/usr/bin/python3

"""
Module defines a function to add double line breaks after certain 
punctuation marks in a text.
"""

# Define a function named "text_indentation" that takes one parameter, "text".
def text_indentation(text):

    """
    Create a new string by replacing specific punctuation marks 
    with the same marks followed by two line breaks.
    """
    new_str_list = (
        text.replace("?", "?\n\n").replace(":", ":\n\n").replace(".", ".\n\n")
    )

    # Print the modified text without adding a newline at the end.
    print(new_str_list, end="")

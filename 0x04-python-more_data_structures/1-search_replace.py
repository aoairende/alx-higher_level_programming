#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # List comprehension to create a new list with replacements.
    return [replace if x == search else x for x in my_list]

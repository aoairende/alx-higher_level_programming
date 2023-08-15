#!/usr/bin/python3

def element_at(my_list, idx):

    # Check if the index is within the bounds of the list.
    if idx >= 0 and idx < len(my_list):
        return my_list[idx]

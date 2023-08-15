#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    # Create a duplicate of the original list to avoid modifying it directly.
    my_list_dup = my_list[:]

    # Check if the index is within the bounds of the duplicated list.
    if idx >= 0 and idx < len(my_list_dup):
        my_list_dup[idx] = element
        return my_list_dup
    return my_list_dup

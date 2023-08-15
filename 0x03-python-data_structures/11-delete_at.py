#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    # # Check if the index is within the valid range of the list.
    if idx >= 0 and idx < len(my_list):

        # Replace the slice at the specified index with an empty list to delete the element.
        my_list[idx:(idx + 1)] = []
    return my_list

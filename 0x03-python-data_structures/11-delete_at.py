#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    # Check if the index is within the valid range of the list.
    if idx < 0 or idx >= len(my_list):
        return my_list

        # Replace the slice at the specified index with an empty list to delete the element.
        del my_list[idx]
        return my_list


    if __name__ == "__main__":
        my_list = [1, 2, 3, 4, 5]
        idx = 3
        new_list = delete_at(my_list, idx)
        print(new_list)
        print(my_list)

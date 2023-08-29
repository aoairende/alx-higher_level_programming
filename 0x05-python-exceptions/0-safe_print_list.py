#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        element = 0

        for i in range(x):
            print(my_list[i], end="")
            element += 1
        print()
    except IndexError:
        print()
    finally:
        return element
#!/usr/bin/python3
if __name__ == "__main__":

    # Import function from calculator_1.py
    from calculator_1 import add, sub, mul, div

    # Assign values for variables a and b
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

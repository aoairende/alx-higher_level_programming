#!/usr/bin/python3
if __name__ == "__main__":

    # Import sys module to access command-line arguments.
    import sys
    # Import module from calculator_1.py
    from calculator_1 import add, sub, mul, div

    args = len(sys.argv) # Get total number of command-line args passed
    argv = sys.argv # Get the list of command-line args
    ops = "+-*/"

    # Check if the correct number of args is provided
    if args != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    # Check if the provided operator is valid
    if ops.find(argv[2]) == -1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if argv[2] == "+":
        print(f"{argv[1]} + {argv[3]} = {add(int(argv[1]), int(argv[3]))}")
    elif argv[2] == "-":
        print(f"{argv[1]} - {argv[3]} = {sub(int(argv[1]), int(argv[3]))}")
    elif argv[2] == "*":
        print(f"{argv[1]} * {argv[3]} = {mul(int(argv[1]), int(argv[3]))}")
    elif argv[2] == "/":
        print(f"{argv[1]} / {argv[3]} = {div(int(argv[1]), int(argv[3]))}")

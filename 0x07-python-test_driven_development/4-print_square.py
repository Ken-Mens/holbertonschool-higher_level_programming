#!/usr/bin/python3
def print_square(size):
    """function to print square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        slash = "#" * (size)
        for idx in range(size):
            print("{}".format(slash))

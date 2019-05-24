#!/usr/bin/python3
def add_integer(a, b=98):
    """add_integer: check for edge cases, otherwise return sum of 2 ints"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))

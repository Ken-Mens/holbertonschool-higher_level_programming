#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    hold = number % 10
    print(hold, end="")
    return hold

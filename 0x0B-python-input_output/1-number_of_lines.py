#!/usr/bin/python3
def number_of_lines(filename=""):
    lin = 0
    with open(filename, encoding="UTF-8") as foo:
        for line in foo:
            lin += 1
    return lin

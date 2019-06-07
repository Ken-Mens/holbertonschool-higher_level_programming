#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    red = 0
    with open(filename, encoding='UTF-8') as foo:
        for line in foo:
            if nb_lines <= 0 or red < nb_lines:
                print(line, end="")
                red = red + 1

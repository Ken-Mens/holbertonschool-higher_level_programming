#!/usr/bin/python3

for x in range(0, 10):
    for y in range(x + 1, 10):
        if (x != 9):
            print("{}".format(x), end="")
            if (x == 8 and y == 9):
                print("{}".format(y))
            else:
                print("{}".format(y), end=", ")

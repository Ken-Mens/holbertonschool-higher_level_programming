#!/usr/bin/python3
def uppercase(str):

    for i in str:
        temp = ord(i)
        if temp >= 97 and temp <= 122:
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print("")

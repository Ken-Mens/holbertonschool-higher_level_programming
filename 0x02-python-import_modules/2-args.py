#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    if (len(sys.argv) == 1):
        print("{}".format("0 arguments."))
    elif (len(sys.argv) == 2):
        print("{}".format("1 argument:"))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    if (len(sys.argv) > 1):
        for og in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1

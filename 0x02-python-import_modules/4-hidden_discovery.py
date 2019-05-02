#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    foo = dir(hidden_4)
    for i in range(0, len(foo)):
        if(foo[i][0] != "_" and foo[i][1] != "_"):
            print("{}".format(foo[i]))

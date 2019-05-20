#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{}".format(value))
    except (ValueError, TypeError) as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return False
    return True

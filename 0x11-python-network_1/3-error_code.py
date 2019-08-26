#!/usr/bin/python3
""" post error code """
import urllib.request as request
import urllib.error as error
import sys


if __name__ == "__main__":
    try:
        req = request.Request(sys.argv[1])
        with request.urlopen(req) as p:
            print(p.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)

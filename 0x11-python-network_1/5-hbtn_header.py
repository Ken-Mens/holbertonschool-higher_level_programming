#!/usr/bin/python3
""" response header"""
import requests
import sys


if __name__ == "__main__":
    part = sys.argv[1]
    re = requests.get(part)
    print(re.headers.get('X-Request-Id'))

#!/usr/bin/python3
""" posts email to params """

from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    data = urlencode({'email': sys.argv[2]}).encode('utf-8')
    part = sys.argv[1]
    req = Request(part, data)

    with urlopen(req) as re:
        print(re.read().decode('utf-8'))

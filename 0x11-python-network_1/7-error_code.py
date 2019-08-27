#!/usr/bin/python3
""" post error code """
import requests
import sys

if __name__ == "__main__":
    part = sys.argv[1]
    re = requests.get(part)
    if re.status_code >= 400:
            print("Error code:", re.status_code)
    else:
        print(re.text)

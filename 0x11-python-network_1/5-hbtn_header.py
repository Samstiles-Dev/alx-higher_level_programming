#!/usr/bin/python3
"""Shows d X-Request-Id header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    f = requests.get(url)
    print(f.headers.get("X-Request-Id"))

#!/usr/bin/python3
"""This code fetches https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    f = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(f.text)))
    print("\t- content: {}".format(f.text))

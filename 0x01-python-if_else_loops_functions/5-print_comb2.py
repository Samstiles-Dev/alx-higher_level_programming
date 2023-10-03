#!/usr/bin/python3
"""prints numbers from 0 to 99"""
for x in range(100):
    print("{:0>2}".format(x), end=", " if x < 99 else "\n")

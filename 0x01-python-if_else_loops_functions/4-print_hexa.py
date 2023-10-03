#!/usr/bin/python3
"""Print numbers from 0 to 98 in decimal and hexadecimal."""
for x in range(0, 99):
    print("{:d} = {}".format(x, hex(x)))

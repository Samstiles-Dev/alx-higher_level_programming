#!/usr/bin/python3
"""program that prints the result of the addition of all arguments"""


import sys
if __name__ == "__main__":
    arg_length = len(sys.argv)
    result = 0
    for k in range(1, arg_length):
        result += int(sys.argv[k])
    print(result)

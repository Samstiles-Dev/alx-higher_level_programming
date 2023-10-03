#!/usr/bin/python3
"""prints the ASCII alphabet, in lowercase, not followed by a new line"""
for char in range(ord('a'), ord('z') + 1):
    print('{}'.format(chr(char)), end='')

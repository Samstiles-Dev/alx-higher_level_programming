#!/usr/bin/python3
"""prints the ASCII alphabet, in lowercase, not followed by a new line"""
for alphabt in range(97, 123):
    if chr(alphabt) != 'q' and chr(alphabt) != 'e':
        print("{}".format(chr(alphabt)), end="")

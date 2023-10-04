#!/usr/bin/python3
"""creates a copy of the string, removing the char at the position n"""


def remove_char_at(str, n):
    if n >= 0:
        return str[:n] + str[n+1:]
    else:
        return str

#!/usr/bin/python3
"""A program that prints the ASCII alphabet, in lowercase, not followed by a new line"""
for char in range(ord('a'), ord('z') + 1):
    print(f"{chr(char)}", end="")

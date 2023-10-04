#!/usr/bin/python3
"""that prints the ASCII alphabet, in reverse order,"""


for i in range(ord('z'), ord('a')-1, -1):
    print('{:c}'.format(i) if i % 2 == 0 else chr(i-32), end='')

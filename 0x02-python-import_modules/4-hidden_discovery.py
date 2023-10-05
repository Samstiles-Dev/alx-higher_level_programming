#!/usr/bin/python3
"""pgm that prints all names defined by the compiled module"""


if __name__ == "__main__":
    import hidden_4
    dirs = dir(hidden_4)
    for i in range(0, len(dirs)):
        if "__" != dirs[i][:2]:
            print(dirs[i])

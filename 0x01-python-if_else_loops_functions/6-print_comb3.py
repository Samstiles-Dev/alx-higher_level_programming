#!/usr/bin/python3
"""prints all possible different combinations of two digits."""
for num_1 in range(10):
    for num_2 in range(10):
        if num_1 < num_2:
            if (num_1 * 10 + num_2) != 89:
                print("{}{},".format(num_1, num_2), end=" ")
            else:
                print("{}{}".format(num_1, num_2))

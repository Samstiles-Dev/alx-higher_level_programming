#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for t in sorted(my_dict.keys()):
        print('{}: {}'.format(t, my_dict[t]))

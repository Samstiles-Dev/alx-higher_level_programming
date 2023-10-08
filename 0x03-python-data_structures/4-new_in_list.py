#!/usr/bin/python3
""" replaces an element in a list at a specific position"""


def new_in_list(my_list, idx, element):
    if not my_list:
        return
    my_new_list = my_list.copy()
    if 0 <= idx < len(my_new_list):
        my_new_list[idx] = element
    return my_new_list

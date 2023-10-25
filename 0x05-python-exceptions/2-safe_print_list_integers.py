#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """this func prts the !st x elem of a list that are ints.

    Args:
        my_list (list): The list to print elem from.
        x (int): The number of elems of my_list to print.

    Returns:
        The number of elems printed.
    """
    result = 0
    for k in range(0, x):
        try:
            print("{:d}".format(my_list[k]), end="")
            result += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (result)

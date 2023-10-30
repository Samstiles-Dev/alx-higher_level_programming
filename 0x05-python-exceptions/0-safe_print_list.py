#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list from which elements is printed.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    result = 0
    for k in range(x):
        try:
            print("{}".format(my_list[k]), end="")
            result += 1
        except IndexError:
            break
    print("")
    return (result)
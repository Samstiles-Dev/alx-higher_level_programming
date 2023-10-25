#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """this Divides two lists element by element.

    Args:
        my_list_1 (list): The 1st list.
        my_list_2 (list): The 2nd list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length that contains all the divisions.
    """
    _n_list = []
    for k in range(0, list_length):
        try:
            _div = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("wrong type")
            _div = 0
        except ZeroDivisionError:
            print("division by 0")
            _div = 0
        except IndexError:
            print("out of range")
            _div = 0
        finally:
            _n_list.append(_div)
    return (_n_list)

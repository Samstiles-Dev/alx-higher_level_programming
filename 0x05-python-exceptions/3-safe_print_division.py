#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        _div = a / b
    except (TypeError, ZeroDivisionError):
        _div = None
    finally:
        print("Inside result: {}".format(_div))
    return (_div)

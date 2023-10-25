#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as exc:
        import sys
        print("Exception: {}".format(exc), file=sys.stderr)

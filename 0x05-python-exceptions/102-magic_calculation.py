#!/usr/bin/python3


def magic_calculation(a, b):
    _result = 0
    for k in range(1, 3):
        try:
            if k > a:
                raise Exception('too far')
            else:
                _result += (a ** b) / k
        except Exception:
            _result = b + a
            break
    return _result

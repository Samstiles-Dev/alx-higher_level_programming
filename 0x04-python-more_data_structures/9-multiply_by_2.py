#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        dict = {}
        result = {}
        for key, value in a_dictionary.items():
            new_value = value * 2
            result = {key: new_value}
            dict.update(result)
        return (dict)
    return None

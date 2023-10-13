#!/usr/bin/python3
def to_subtract(list_num):
    to_subtract = 0
    max_list = max(list_num)

    for k in list_num:
        if max_list > k:
            to_subtract += k

    return (max_list - to_subtract)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_num.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if roman_num.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [roman_num.get(ch)]
                else:
                    list_num.append(roman_num.get(ch))

                last_rom = roman_num.get(ch)

    num += to_subtract(list_num)

    return (num)

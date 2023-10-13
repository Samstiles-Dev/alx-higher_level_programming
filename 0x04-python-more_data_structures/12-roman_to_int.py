#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    dict_data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = [dict_data[x] for x in roman_string] + [0]
    count = 0

    for k in range(len(nums) - 1):
        if nums[k] >= nums[k+1]:
            count += nums[k]
        else:
            count -= nums[k]

    return count

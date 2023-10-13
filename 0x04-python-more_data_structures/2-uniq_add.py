#!/usr/bin/python3
def uniq_add(my_list=[]):
    grand_list = 0
    for k in set(my_list):
        grand_list += k
    return(grand_list)

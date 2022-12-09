#!/usr/bin/python3
def uniq_add(my_list=[]):
    summ = 0
    for x in set(my_list):
        summ += x
        return (summ)

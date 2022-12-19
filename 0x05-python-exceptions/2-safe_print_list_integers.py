#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    for k in range(0, x):
        try:
            print("{:d}".format(my_list[k]), end="")
            ret += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (ret) # ret is the number of elements printed

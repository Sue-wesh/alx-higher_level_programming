#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num = len(argv) - 1

    if (num == 0):
        print("{} arguments.".format(num))

    elif (num == 1):
        print("{} argument:".format(num))

    else:
        print("{} arguments:".format(num))

    for x in range(1, len(argv)):
        print("{}: {}".format(x, argv[x]))

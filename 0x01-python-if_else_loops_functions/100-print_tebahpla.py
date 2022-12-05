#!/usr/bin/python3
i = 0
for x in range(122, 97-1, -1):
    print("{}".format(chr(x-i)), end="")
    i = 32 if i == 0 else 0

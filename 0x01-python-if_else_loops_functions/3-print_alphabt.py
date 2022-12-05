#!/usr/bin/python3
for x in range(97, 122):
    if x == ord(e) or x == ord(q):
        continue
    print("{:c}".format(chr(x)), end="")

#!/usr/bin/python3

Rectangle = __import__('4-rectangle').Rectangle
rect = Rectangle(2, 4)
print(str(rect))
print("--")
print(rect)
print("--")
print(repr(rect))
print("--")
print(hex(id(rect)))
print("--")

new_rect = eval(repr(rect))
print(str(new_rect))
print("--")
print(new_rect)
print("--")
print(repr(new_rect))
print("--")
print(hex(id(new_rect)))
print("--")

print(new_rect is rect)
print(type(new_rect) is type(rect))

#!/usr/bin/python3

"""define a class Square that inherits from the class Rectangle."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """represents a Square.
    .. it inherits from Rectangle
    .. class constructor def __init__(self, size, x=0, y=0, id=None)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize size, x, y and id for a new Square."""
        
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

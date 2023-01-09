#!/usr/bin/python3

"""defines a class MyInt that inherits from int"""

class MyInt(int):
    """represents class MyInt whic has operators == and != inverted"""

    def __eq__(self, value):
        """for === operator"""

        return self.real != value

    def __ne__(self, value):
        """ for != operator"""

        return self.real == value

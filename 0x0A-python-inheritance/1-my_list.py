#/usr/bin/python3

"""defines a class MyList that inherits from list."""

class MyList(list):
    """method that prints the list in ascending sort."""
    def print_sorted(self):
        """print a list in ascending order."""
        print(sorted(self))

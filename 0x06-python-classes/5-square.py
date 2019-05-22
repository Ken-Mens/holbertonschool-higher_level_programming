#!/usr/bin/python3
class Square:
    """A Square class."""

    def __init__(self, size=0):
        """Initialize the size"""
        self.size = size

    @property
    def size(self):
        """Getter for Square."""
        return self.__size

    @size.setter
    def size(self, value):
        "Setter for Square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return area of Square."""
        return self.__size ** 2

    def my_print(self):
        """"Print the square to stdout."""
        if self.__size == 0:
            print()
        else:
            slash = "#" * (self.size)
            for idx in range(self.size):
                print("{}".format(slash))

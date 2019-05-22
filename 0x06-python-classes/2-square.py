#!/usr/bin/python3
"""Defines a Square class that defines a square by previous parameters"""


class Square:
    """Creates Square class"""

    def __init__(self, size=0):
        """Initializes Square"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

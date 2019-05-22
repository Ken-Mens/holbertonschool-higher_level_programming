#!/usr/bin/python3
"""Defines a Square type with previous size"""


class Square:
    """ Square class with private instane"""

    def __init__(self, size=0):
        """Initializes Square"""
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Returns square area of Square"""
        return self.__size ** 2

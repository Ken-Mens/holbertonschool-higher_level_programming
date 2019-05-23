#!/usr/bin/python3
class Square:
    """creates square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialization with size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """finds size"""
        return self.__size

    @size.setter
    def size(self, value):
        """validates size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """finds area of Square"""
        return (self.__size ** self.__size)

    @property
    def position(self):
        """finds position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position value"""
        if type(value) != tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """prints square with character # in stdout"""
        if self.__size == 0:
            print()
            return

        for x in range(self.position[1]):
            print()

        for y in range(self.__size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))

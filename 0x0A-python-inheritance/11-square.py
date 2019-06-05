#!/usr/bin/python3
class BaseGeometry:

    def area(self):
        return self.__size * self.__size

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0.'.format(name))
        else:
            if name == 'width':
                self.__width = value
            if name == 'height':
                self.__height = value
            if name == 'size':
                self.__size = value


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    def __str__(self):
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator('size', size)
        self.__size = size

    def __str__(self):
        return '[Square] {}/{}'.format(self.__size, self.__size)

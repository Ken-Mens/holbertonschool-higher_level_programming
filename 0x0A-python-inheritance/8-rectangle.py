#!/usr/bin/python3
class BaseGeometry:
    def __init__(self, width, height):
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0.'.format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)

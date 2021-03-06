#!/usr/bin/python3
class Rectangle:
    """ This class will define a Rectangle """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        perimeter = ((self.width + self.height) * 2)
        return (perimeter)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        width = 0
        width = "#" * self.width
        rectangle = width
        for x in range(self.height - 1):
            rectangle += "\n" + width
        return rectangle

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        del self
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

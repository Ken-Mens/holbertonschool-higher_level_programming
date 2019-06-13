#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Checks Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Checks to initialize"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Checks width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Checks width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Checks height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Checks height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Checks x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Checks x value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Checks y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Checks y value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Checks area"""
        return self.__width * self.__height

    def display(self):
        """Checks display"""
        print("\n" * self.y, end="")
        for a in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)

    def __str__(self):
        """Checks str"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Checks update"""
        Attri = ["id", "width", "height", "x", "y"]
        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)
        for idx, arg in enumerate(args):
            setattr(self, Attri[idx], arg)

    def to_dictionary(self):
        """Checks dictionary"""
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return (dic)

#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherited from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Init class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """Checks size"""
        return (self.height)

    @size.setter
    def size(self, value):
        """Checks size value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Checks update"""
        Attri = ["id", "size", "x", "y"]
        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)
        for idx, arg in enumerate(args):
            setattr(self, Attri[idx], args[idx])
            idx += 1

    def to_dictionary(self):
        """Checks dictionary"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return (dic)

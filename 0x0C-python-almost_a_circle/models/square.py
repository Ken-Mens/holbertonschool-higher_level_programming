#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        return (self.height)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        Attri = ["id", "size", "x", "y"]
        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)
        for idx, arg in enumerate(args):
            setattr(self, Attri[idx], args[idx])
            idx += 1

    def to_dictionary(self):
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return (dic)

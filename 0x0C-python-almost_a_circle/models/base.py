#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        op = []
        if list_objs is not None:
            for idx in list_objs:
                op.append(cls.to_dictionary(idx))
        with open(filename, "w", encoding='utf-8') as foo:
            foo.write(cls.to_json_string(op))

    def from_json_string(json_string):
        if json_string is None:
            json_string = []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        tempo = cls(1, 1)
        tempo.update(**dictionary)
        return (tempo)

    @classmethod
    def load_from_file(cls):
        fn = cls.__name__ + ".json"
        lst = []
        try:
            with open('{}.json'.format(cls.__name__), 'r') as foo:
                lst = cls.from_json_string(foo.read())
            for x, y in enumerate(lst):
                lst[x] = cls.create(**lst[x])
        except:
            pass
        return (lst)

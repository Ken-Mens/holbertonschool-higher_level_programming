#!/usr/bin/python3
class Student():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            return ({keys: doors for keys, doors in self.__dict__.items()
                    if keys in attrs})

    def reload_from_json(self, json):
        self.__dict__.update(json)
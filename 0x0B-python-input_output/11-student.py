#!/usr/bin/python3
''' module tat defines a class '''


class Student:
    '''class that defines a student '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            new_attr = {}
            for attr in attrs:
                if attr in self.__dict__:
                    new_attr[attr] = self.__dict__[attr]
            return new_attr

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

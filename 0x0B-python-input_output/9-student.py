#!/usr/bin/python3
''' module tat defines a class '''


class Student:
    '''class that defines a student '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = name
        self.age = age

    def to_json(self):
        return (self.__dict__)

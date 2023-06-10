#!/usr/bin/python3

"""function that returns available attributes
and methods of an object """


def lookup(obj):
    """ takes an object and returns
    a list of its attributes and methods """

    return dir(obj)

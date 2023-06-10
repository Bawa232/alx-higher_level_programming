#!/usr/bin/python3

""" function that checks if an
object is an instance of a class """


def is_same_class(obj, a_class):
    """ returns true if the object is an instance
    of the class, otherwise, return false """

    if isinstance(obj, a_class):
        return True
    else:
        return False

#!/usr/bin/python3

''' function that checks if a class
is a subclass of another class '''


def inherits_from(obj, a_class):
    '''returns True if the object inherits
    directly or indirectly from another class

    Args:
        obj(object)
        a_class(class)
    '''

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True

    return False

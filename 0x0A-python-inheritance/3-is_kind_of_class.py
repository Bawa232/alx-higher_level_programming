#!/usr/bin/python3

""" function that checks if an object
is an instance of a class """


def is_kind_of_class(obj, a_class):
    """ returns true if the object is
    an instance of the class

    Args
        obj(object)
        (a_class)
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False

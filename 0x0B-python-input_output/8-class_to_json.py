#!/usr/bin/python3
''' working with classes and json '''


def class_to_json(obj):
    ''' Args:
            obj(instance)
        Returns:
            dictionary description of the object
    '''

    return (obj.__dict__)

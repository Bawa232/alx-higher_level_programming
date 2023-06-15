#!/usr/bin/python3
''' working with classes and json '''
import json


def class_to_json(obj):
    ''' Args:
            obj(instance)
        Returns:
            dictionary description of the object
    '''

    return json.dumps(obj.__dict__)

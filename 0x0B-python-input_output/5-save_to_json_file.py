#!/usr/bin/python3
''' writing a json rep of an
object to a file '''
import json


def save_to_json_file(my_obj, filename):
    '''Args:
        my_obj(python obj): python object
        to be converted to json
        filename: name of file to store
        the string rep of the object
    '''

    with open(filename, 'w') as f:
        json.dump(my_obj, f)

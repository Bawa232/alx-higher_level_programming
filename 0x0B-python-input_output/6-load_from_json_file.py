#!/usr/bin/python3
''' writing a json rep of an
object to a file '''
import json


def load_from_json_file(filename):
    '''Args:
        filename: name of file to store
        the obj rep of the string
    '''

    with open(filename) as f:
        json.load(f)

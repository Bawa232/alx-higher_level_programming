#!/usr/bin/python3
'''converting json to python '''
import json


def from_json_string(my_str):
    '''Args:
        my_str(string): json string

        Returns:
        A python object
    '''

    return json.loads(my_str)

#!/usr/bin/python3
""" nodule that reads textfiles """


def read_file(filename=""):
    '''function that takes in a
    filename as perimeter and reads it'''

    with open(filename, encoding="utf-8") as f:
        print(f.read())

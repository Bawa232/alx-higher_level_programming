#!/usr/bin/python3
''' script that appends to a file '''


def append_write(filename="", text=""):
    ''' function thst sppends to a file
    Args:
        filename(string): name of the file tof be appended
        text(string): text to be added to te file

    Returns
        number of characters added
    '''

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

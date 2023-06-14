#!/usr/bin/python3
""" modules that show how to
write to a file """


def write_file(filename="", text=""):
    """ function writes to a file
    Args:
        Filename(string): file to be created
        text(string): text to be written to file

    Returns:
        number of character written
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)

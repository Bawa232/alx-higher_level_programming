#!/usr/bin/python3
""" creating a class rectangle and initializing
    it with a width and height
"""


class Rectangle:
    """ A Rectangle class that initializes a width and height """

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        """ method that retrieves the private instance
        attribute - width """

        return self._width

    @width.setter
    def width(self, value):
        """ a method that sets the value of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self._width = value

    @property
    def height(self):
        """ method that retrieves the attribute - width """
        return self._height

    @height.setter
    def height(self, value):
        """ method that sets the value of height """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self._height = value

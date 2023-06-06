#!/usr/bin/python3
""" creating a class rectangle and initializing
    it with a width and height
"""


class Rectangle:
    """ A Rectangle class that initializes a width and height """

    def __init__(self, width, height):
        """ Initialize an instance of the class Rectangle.
        Args:
            width(int): width of the rectangle
            height(int): Height of the rectangle
        Raises:
            TypeError: width must be an integer
            TypeError: height must be an integer
            ValueError: width must be >= 0
            ValueError: height must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that retrieves the private instance
        attribute - width """

        return self.__width

    @width.setter
    def width(self, value):
        """ a method that sets the value of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ method that retrieves the attribute - width """
        return self.__height

    @height.setter
    def height(self, value):
        """ method that sets the value of height """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

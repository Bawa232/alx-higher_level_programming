#!/usr/bin/python3
"""
A module that sets size of square as private field

"""


class Square:
    """Square class

    private instance field(s) : size
    methods: __init__

    """

    def __init__(self, size=0):
        """initializes the class

        Args:
            size (int, optional): size of square. Defaults to 0.
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            Args: it takes no arguments

            Return: It returns the size of the area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ Takes no arguments and returns the size of the area"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method to set the value of the size"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

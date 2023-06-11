#!/usr/bin/python3
""" module that impliments a class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' A class 'square' that takes
    a Rectnngle class as its base class '''
    def __init__(self, size):
        '''initializes the class
        Args:
            size(int)
        '''
        self.integer_validator("size", size)
        self._size = size
        super().__init__(size, size)

    def area(self):
        '''returns area of the quare class '''
        return self._size ** 2

    def __str__(self):
        '''special method that returns
        the string representation of
        an object '''

        return "[Square] {}/{}".format(size, size)

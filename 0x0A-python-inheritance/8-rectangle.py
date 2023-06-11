#!/usr/bin/python3

""" creates a class named BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' subclass of BaseGeomety '''

    def __init__(self, width, height):
        ''' initializes Rectangle
        Args:
            width(int): width of the rectangle
            height: height of the reectangle
        '''
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height

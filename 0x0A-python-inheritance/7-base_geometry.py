#!/usr/bin/python3

""" creates a class named BaseGeometry """


class BaseGeometry:
    ''' creates 2 method self and inteer_validator '''
    def area(self):
        ''' raises an exception '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' validates value to be an int
            Args:
                name(string)
                value(int)
                '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

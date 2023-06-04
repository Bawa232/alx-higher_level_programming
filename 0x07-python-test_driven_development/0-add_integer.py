#!/usr/bin/python3
""" module to find the sum of two numbers """


def add_integer(a, b=98):
    """
        args a: takes an integer or float and returns a TypeError otherwise
            b: instantiated to 98

        Returns: int(a + b)

    """

    if a is None:
        raise TypeError("a must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)

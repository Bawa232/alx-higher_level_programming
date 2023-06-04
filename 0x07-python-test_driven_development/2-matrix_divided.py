#!/usr/binn/python3
""" module that divides all elements in a matrix """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number
        Args:
            matrix; a list of lists of integers or float
            div; a number to divide the element of the matrix with

        Returns:
            A new list of numbers divided by div and rounded
            to 2 decimal places

        Raises:
            TypeError: if matrix is not a list of lists
            TypeError: if elements in each row of matrix are not int or float
            ZeroDivisionError: if div is zero

    """
    s = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        if not isinstance(row, list) for row in matrix:
            raise TypeError(s)

    if any(len(row) != len(matrix[0]) for row in matrix:
        raise TypeError("Each row of the matrix must have the same size")

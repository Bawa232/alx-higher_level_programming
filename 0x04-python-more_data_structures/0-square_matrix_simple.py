#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    if(matrix):
        return list(map(lampda innerL: [x**2 for x in innerL], matrix))

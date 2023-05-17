#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    power = []

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            power.append(matrix[i][j] ** 2)

    return power

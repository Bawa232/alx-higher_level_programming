#!/usr/bin/python3

def best_score(a_dictionary):

    best_score = None
    maxVal = -inf

    for key, value in a_dictionary.items():
        if value > maxVal:
            maxVal = value
            best_score = key

    return best_score

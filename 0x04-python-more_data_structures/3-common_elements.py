#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_set1 = list(set_1)
    new_set2 = list(set_2)
    new = []

    for i in range(len(new_set1)):
        for j in range(len(new_set2)):
            if new_set1[i] == new_set[2]:
                new.append(new_set1[i])

    return set(new)

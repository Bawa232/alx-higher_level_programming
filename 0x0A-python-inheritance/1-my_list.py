#!/usr/bin/python3

""" class thas a subclass of the list ckass """


class MyList(list):
    """ class that prints elements of a list
    in ascening order """
    def print_sorted(self):
        """ function that prints a sorted list """

        sortList = sorted(self)
        print(sortList)

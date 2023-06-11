#!/usr/bin/python3
""" creates a class called Mylist """


class MyList(list):

    """ defines a function called print_sorted with a self attribute """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        print(sorted(self))

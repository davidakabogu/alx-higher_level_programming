#!/usr/bin/python3
""" defines a function called lookup with an object attribute """


def lookup(obj):
    """ returns the list of available attributes and methods of an object """
    return dir(obj)

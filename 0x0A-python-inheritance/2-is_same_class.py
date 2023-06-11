#!/usr/bin/python3
""" defines a function called is_same_class with obj, a_class attributes """


def is_same_class(obj, a_class):
    """ returns True if object is exactly an instance of the specified class
    otherwise False
    """

    return True if type(obj) == a_class else False

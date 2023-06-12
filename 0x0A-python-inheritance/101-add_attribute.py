#!/usr/bin/python3
""" defines a function called add_attribute """


def add_attribute(obj, att, value):
    """
    adds a new attribute to an object if it's possible.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of the attribute.
    Raises:
        TypeError: if the object can’t have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

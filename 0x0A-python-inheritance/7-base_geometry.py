#!/usr/bin/python3
""" creates a class called BaseGeometry """


class BaseGeometry:
    """ defines a function called area with self attribute """
    def area(self):
        """ not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

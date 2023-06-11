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


""" creates a class Rectangle that inherits from BaseGeometry """


class Rectangle(BaseGeometry):
    """ defines instantiation with width and height """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

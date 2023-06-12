#!/usr/bin/python3
""" imports a class called BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" creates a class Rectangle that inherits from BaseGeometry """


class Rectangle(BaseGeometry):
    """ defines instantiation with width and height """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """ this function defines the area of a retangle """
    def area(self):
        return self.__width * self.__height

    """
    this function print() should print, and str() should return,
    the following rectangle description: [Rectangle] <width>/<height>
    """
    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

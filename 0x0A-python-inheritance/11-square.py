#!/usr/bin/python3
""" imports a class called Rectangle """
Rectangle = __import__('9-rectangle').Rectangle

""" creates a class Square that inherits from Rectangle """


class Square(Rectangle):
    """ defines Instantiation with size """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

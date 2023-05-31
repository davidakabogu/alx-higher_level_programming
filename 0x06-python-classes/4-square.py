#!/usr/bin/python3


class Square:
    """ Represents a square. """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """ Gets or sets the current size of the square. """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Validates and sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates and returns the area of the square. """
        return self.__size ** 2

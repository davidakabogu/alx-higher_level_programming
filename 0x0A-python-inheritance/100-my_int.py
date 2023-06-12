#!/usr/bin/python3
""" creates a class called MyInt that inherits from int """


class MyInt(int):
    """ Inverts the operators == and != """

    def __eq__(self, value):
        """Override == opeartor with != operator """
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == operator """
        return self.real == value

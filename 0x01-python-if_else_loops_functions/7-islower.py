#!/usr/bin/python3

def islower(c):
    """Function checks for lowercase characters."""
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False

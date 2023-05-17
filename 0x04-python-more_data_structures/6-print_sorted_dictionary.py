#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_dict = list(a_dictionary.keys())
    ord_dict.sort()
    for i in ord_dict:
        print("{}: {}".format(i, a_dictionary.get(i)))

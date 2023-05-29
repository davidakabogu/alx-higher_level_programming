#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first specified number of elements from a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements from my_list to print.

    Returns:
        The number of elements actually printed.
    """
    printed_count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return printed_count

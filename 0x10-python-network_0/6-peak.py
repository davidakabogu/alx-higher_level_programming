#!/usr/bin/python3
# this function finds a peak in a list of unsorted integers.
# a peak is a number that is greater than its adjacent numbers

def find_peak(list_of_integers):

    # # check if list is empty
    # if not list_of_integers:
    #     return None
    
    # # check is list is single digit
    # if len(list_of_integers) == 1:
    #     return list_of_integers[0]

    # # iterate through list
    # for i in range(1, len(list_of_integers) - 1):
    #     if (list_of_integers[i] > list_of_integers[i + 1] and
    #             list_of_integers[i] > list_of_integers[i - 1]):
    #         return list_of_integers[i]

    # # check first and last elements as the have only one neighbor
    # if list_of_integers[0] >= list_of_integers[1]:
    #     return list_of_integers[0]
    # if list_of_integers[-1] >= list_of_integers[-2]:
    #     return list_of_integers[-1]

    # return None  # no peak found
    if list_of_integers is None or list_of_integers == []:
        return None
    lo = 0
    hi = len(list_of_integers)
    mid = ((hi - lo) // 2) + lo
    mid = int(mid)
    if hi == 1:
        return list_of_integers[0]
    if hi == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

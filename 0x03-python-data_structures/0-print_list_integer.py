#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """function that prints integers in a list."""
    for j in range(len(my_list)):
        print('{:d}'.format(my_list[j]))

""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""


def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    file_open = open(filename)
    file_read = file_open.read()
    file_read = file_read.strip()
    file_list = file_read.split()
    print file_list



def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """




    pass


fruits_list_1 = open_and_read_file("fruits_1.txt")
fruits_list_2 = open_and_read_file("fruits_2.txt")

compare(fruits_list_1, fruits_list_2)


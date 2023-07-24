#!/usr/bin/env python3

"""
index range
"""


def index_range(page, page_size):
    """ a function that can return a tuple"""
    new_list = []
    new_list.append((page_size * page) - page_size)
    new_list.append(page_size * page)
    return tuple(new_list)

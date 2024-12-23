#!/usr/bin/env python3
"""
Simple helper functions for pagination
"""


def index_range(page: int, page_size: int):
    """
    Return a tuple of size two containing start index and end index
    """
    return ((page - 1) * page_size, page * page_size)

#!/usr/bin/env python3
""" FIFO cache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """basic cache defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            first, _ = self.cache_data.popitem(last=True)
            print("DISCARD: {}".format(first))

    def get(self, key):
        """Get an item by key"""
        # if key is None or key not in self.cache_data:
        #     return None
        # else:
        return self.cache_data.get(key, None)

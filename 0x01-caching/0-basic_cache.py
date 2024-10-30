#!/usr/bin/env python3
""" Base cache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic cache defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if (key or item) is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        # if key is None or key not in self.cache_data:
        #     return None
        # else:
        return self.cache_data.get(key, None)

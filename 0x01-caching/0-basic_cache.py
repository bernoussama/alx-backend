#!/usr/bin/python3
""" Base cache module
"""


class BaseCaching:
    """BaseCaching defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    MAX_ITEMS = 4

    def __init__(self):
        """Initiliaze"""
        self.cache_data = {}

    def print_cache(self):
        """Print the cache"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item in the cache"""
        raise NotImplementedError(
            "put must be implemented in your cache class"
        )

    def get(self, key):
        """Get an item by key"""
        raise NotImplementedError(
            "get must be implemented in your cache class"
        )


class BasicCache(BaseCaching):
    """basic cache defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        if (key or item) is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
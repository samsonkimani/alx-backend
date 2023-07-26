#!/usr/bin/env python3

"""
lifo -
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ lifo caching"""

    def __init__(self):
        """ initializing the init method"""
        super().__init__()

    def put(self, key, item):
        """ method to add elements into the cache_data"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                last_key = next(reversed(self.cache_data))
                self.cache_data.pop(last_key)
                print("DISCARD: {}".format(last_key))
            else:
                self.cache_data[key] = item
        self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        """ return the dictionary item"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

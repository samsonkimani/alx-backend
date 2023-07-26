#!/usr/bin/env python3

"""
lifo  caching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ lifo caching"""

    def __init__(self):
        """ initializing the init method"""
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """ method to add elements into the cache_data"""
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.key_indexes.remove(key)
                else:
                    del self.cache_data[self.key_indexes[self.MAX_ITEMS - 1]]
                    item_discarded = self.key_indexes.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """ return the dictionary item"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

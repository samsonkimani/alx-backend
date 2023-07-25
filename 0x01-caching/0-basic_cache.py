#!/usr/bin/usr python3

"""
basic caching model
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ implementing the basic cache class"""

    def __init__(self):
        """ creating the init function"""
        super().__init__()

    def put(self, key, item):
        """ method to add data into the cache data"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        """ method to retirn the value of a given key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

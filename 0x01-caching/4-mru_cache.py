#!/usr/bin/env python3
"""
MRU Caching algorithm
"""


from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    implementing the mru caching algorithm
    """

    def __init__(self):
        """ initializing the mru class"""
        super().__init__()
        self.mru_order = OrderedDict()

    def put(self, key, item):
        """
        Add data into the cache_data based on the most recently used
        item
        """
        if not key or not item:
            return

        self.cache_data[key] = item
        self.mru_order[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.mru_order))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.mru_order) > BaseCaching.MAX_ITEMS:
            self.mru_order.popitem(last=False)

        self.mru_order.move_to_end(key, False)

    def get(self, key):
        """
        return the item based on key given
        """
        if key in self.cache_data:
            self.mru_order.move_to_end(key, False)
            return self.cache_data[key]
        return None

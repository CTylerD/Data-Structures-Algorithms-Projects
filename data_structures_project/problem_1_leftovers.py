# old response - takes linear time
    def set(self, key, value):
        # make room if cache at capacity
        if self.is_full():
            lru_value = self.lru_order.pop(0)
            self.cache.pop(lru_value)
            self.size -= 1
        # add value to hash table
        self.cache[key] = value
        self.size += 1
        # update LRU access array order
        self.lru_order.append(key)
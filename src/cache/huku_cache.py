class HukuInMemoryCache():
    def __init__(self):
        self.cache = {}

    def set(self, key, value, expire_time=None):
        self.cache[key] = value

    def get(self, key):
        return self.cache.get(key)

    def delete(self, key):
        self.cache.pop(key)

    def clear(self):
        self.cache.clear()

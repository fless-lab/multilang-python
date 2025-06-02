class TranslationCache:
    def __init__(self, max_size=1000):
        """Initialize cache with a maximum size."""
        self.cache = {}
        self.max_size = max_size

    def get(self, key):
        """Retrieve cached translation."""
        return self.cache.get(key)

    def set(self, key, value):
        """Cache a translation."""
        if len(self.cache) >= self.max_size:
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = value
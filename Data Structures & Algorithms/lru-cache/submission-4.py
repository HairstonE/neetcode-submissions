class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            res = self.cache.pop(key)
            self.cache[key] = res
            return res
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

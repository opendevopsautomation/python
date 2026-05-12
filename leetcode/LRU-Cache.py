class LRUCache:
    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
    def get(self, key: int) -> int:
        if key in self.cache:
            val=self.cache.pop(key) 
            self.cache[key]=val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys():
            if self.capacity==len(self.cache):
                del self.cache[next(iter(self.cache))]
        else:
            self.cache.pop(key)
        self.cache[key]=value
       
        # if key not in self.cache.keys():
        #     if len(self.cache.keys()) == self.capacity:
        #         del self.cache[next(iter(self.cache))]
        # else:
        #     self.cache.pop(key)
        # self.cache[key] = value

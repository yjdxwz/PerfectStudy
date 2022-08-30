import threading
import weakref

class Bigdata:
    def __init__(self, key):
        pass


# 缓存机制
class Cache:
    def __init__(self):
        self.pool = {}
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            data = self.pool.get(key)
            if data:
                return data
            data = Bigdata(key)
            self.pool[key] = data
            return data

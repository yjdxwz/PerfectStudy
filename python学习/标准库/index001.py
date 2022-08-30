import threading
import weakref

class Bigdata:
    def __init__(self, key):
        pass


# 缓存机制
#  字典, 缓存对象, 强引用
class Cache:
    def __init__(self):
        # 弱引用字典 不会对内部对象产生强引用, 而是一个弱引用,当垃圾回收 ,
        # 判定一个对象是否要被垃圾回收的时候, 不需要考虑弱引用问题,
        # 只要强引用消失 , 就可以被垃圾回收, 为0 就
        self.pool = weakref.WeakKeyDictionary()
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            data = self.pool.get(key)
            if data:
                return data
            data = Bigdata(key)
            self.pool[key] = data
            return data

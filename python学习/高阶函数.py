import random


class BingoCage:
    def __init__(self, items):
        # 在本地构建一个副本, 防止列表参数的意外副作用
        self._items = list(items)
        print("初始化:", self._items)

        random.shuffle(self._items)
        print("初始化后:", self._items)

    def pick(self):
        try:
            value = self._items.pop()
            print("弹出值为:" ,value)
            print("剩余值为",self._items)
            return value
        except IndexError:
            raise LookupError("pick from empty BingoCase")

    def __call__(self, *args, **kwargs):
        # bingo.pick()
        # 的快捷方式是
        # bingo()。
        return self.pick()
# >>> bingo = BingoCage(range(3))
# >>> bingo.pick()
# 1
# >>> bingo()
# 0
# >>> callable(bingo)
# True
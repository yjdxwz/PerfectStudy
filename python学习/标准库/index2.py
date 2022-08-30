import weakref
import sys

class C:
    def __init__(self, value):
        self.value = value


def test_weak_value_dict():
    d = weakref.WeakValueDictionary()
    # d = dict()
    k1 = 'test1'
    v1 = C(1)
    d[k1] = v1
    print(d[k1])

    del v1
    print(d[k1])

test_weak_value_dict()
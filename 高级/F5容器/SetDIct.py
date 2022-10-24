from collections.abc import Mapping, MutableMapping
from collections import abc

# dict 属于Mapping 类型
print(isinstance(dict(), MutableMapping))  # => True  MutableMapping.register(dict)
# dict_method
s = {"a", "b"}
s.add("3333")
print(s)
s1 = frozenset("abcded")
print(s1)  # set 无序


aa = s.difference(s1)
print(aa)
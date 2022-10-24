from collections import abc
aa = list()
a = [1, 2]
c = a + [3, 4] # 两个list 连接起来
print(id(a))

# __iadd__
a += (3, 4) # += 则是 实现了类函数的 __iadd__ 函数 ， __iadd__ 函数包含了extend 函数， 迭代， for
print(c)
print(a)
print(id(a))

# a.append(2)
a.extend("abc")
print(a)
def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print("-> coroutin received ",x)


my_coro = simple_coroutine()

print(my_coro)

next(my_coro)
#  只有暂停状态才能使用 .send方法
my_coro.send(42)


# next(my_coro)
# <generator object simple_coroutine at 0x10c76ff90>
# -> coroutine started
# my_coro.send(43)
# Traceback (most recent call last):
#   File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/code.py", line 90, in runcode
#     exec(code, self.locals)
#   File "<input>", line 1, in <module>
# StopIteration
# -> coroutin received  43

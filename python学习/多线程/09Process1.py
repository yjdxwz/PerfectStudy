import math
import random
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from functools import reduce

ISPRIMS = [random.randint(3,999) for line in range(100)]



def is_prm(n:list):
    sum2 = reduce(lambda x, y: x+y, ISPRIMS)
    # 使用 lambda 匿名函数

    return sum2


def Single():
    is_prm(ISPRIMS)


def threadingppool():
    with ThreadPoolExecutor() as pool:
        pool.submit(is_prm, ISPRIMS)


def ProcessExcute():
    with ProcessPoolExecutor() as pool:
        pool.submit(is_prm, ISPRIMS)


if __name__ == '__main__':
    start = time.time()
    ProcessExcute()
    end = time.time()
    print(f"多进程话费 时间{end - start} s")


    start = time.time()
    Single()
    end = time.time()
    print(f"单线程话费 时间{end - start} s")



    start = time.time()
    threadingppool()
    end = time.time()
    print(f"多线程话费 时间{end - start} s")
    # for line


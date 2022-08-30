import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

ISPRIMS = [112272535095293] * 100


def is_prm(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sort_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sort_n + 1, 2):
        if n% i == 0:
            return False

    return True


def Single():
    for line in ISPRIMS:
        is_prm(line)


def threadingppool():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prm, ISPRIMS)


def ProcessExcute():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prm, ISPRIMS)


if __name__ == '__main__':

    start = time.time()
    Single()
    end = time.time()
    print(f"单线程话费 时间{end - start} s")



    start = time.time()
    threadingppool()
    end = time.time()
    print(f"多线程话费 时间{end - start} s")
    # for line

    start = time.time()
    ProcessExcute()
    end = time.time()
    print(f"多进程话费 时间{end - start} s")


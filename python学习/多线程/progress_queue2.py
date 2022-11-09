from multiprocessing import Process, Queue, Manager, Pipe

import time


# multiprocessing 中的queue 不能用于 pool 进程池

# pool 中的进程间通信 需要使用 manager 中 queue


# from queue import Queue
# from multiprocessing import Queue
# from multiprocessing import Manager
# Manager().Queue()


# 管道通信
# 通过 Pipe 实现进程间通信
# pip 性能高于 queue

def producer(pipe):
    pipe.send("boby")


def cusumer(pipe):
    print(pipe.recv())


if __name__ == '__main__':
    recevie_pipe, send_pipe = Pipe()

    # pipe 只能适用月 两个进程
    my_producer = Process(target=producer, args=(send_pipe,))
    my_cusumer = Process(target=cusumer, args=(recevie_pipe,))

    my_producer.start()
    my_cusumer.start()

    my_producer.join()
    my_cusumer.join()

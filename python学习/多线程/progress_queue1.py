from multiprocessing import Process, Queue, Manager
import time


# 共享全局变量

def producer(a):
    a += 1
    time.sleep(2)


def consumer(a):
    time.sleep(2)
    print(a)


#
# def producer(queue):
#     queue.put("a")
#
# def consumer(queue):
#     data = queue.get()
#     print(data)

if __name__ == '__main__':
    a = 1
    queue = Queue(10)
    my_producer = Process(target=producer, args=(a,))
    my_cusumer = Process(target=consumer, args=(a,))

    my_producer.start()
    my_cusumer.start()

    my_producer.join()
    my_cusumer.join()

    print(a)

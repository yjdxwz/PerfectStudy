from multiprocessing import Process ,Queue, Manager

import time

def producer(queue):
    queue.put("a")

def cusumer(queue):
    data = queue.get()
    print(data)

if __name__ == '__main__':
    queue = Queue(10)
    my_producer = Process(target= producer, args=(queue,))
    my_cusumer = Process(target= cusumer, args=(queue,))

    my_producer.start()
    my_cusumer.start()

    my_producer.join()
    my_cusumer.join()

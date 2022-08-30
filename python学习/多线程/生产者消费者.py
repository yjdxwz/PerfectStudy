import queue
import threading

from python学习.多线程 import SingleThread
import random
import time
def do_crow(url_que:queue.Queue,html_queue:queue.Queue):
    while True:
        url = url_que.get()
        html = SingleThread.getCrow(url)
        html_queue.put(html)
        print(f"current Threading Name {threading.current_thread().name}, Crow URL {url}  urlQue Size {url_que.qsize()}")
        time.sleep(random.randint(1,3))


def do_parse(html_queue:queue.Queue, fout):
    while True:
        html = html_queue.get()
        results= SingleThread.parse(html)
        for result in results:
            fout.write(str(result)+"\n")
        print(f"current Threading Name {threading.current_thread().name}, results Size {len(results)}  html_queue Size {html_queue.qsize()}")
    time.sleep(random.randint(1, 3))



if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in SingleThread.urls:
        url_queue.put(url)
    for idx in range(3):
        t = threading.Thread(target=do_crow,args=(url_queue,html_queue),name=f"crow{idx}")
        t.start()

    fout = open(f"a.txt","w")
    for line in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue,fout),name=f"parse{line}")
        t.start()



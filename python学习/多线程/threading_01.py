import threading
import requests

import time

start = time.time()
urls = [f"https://www.cnblogs.com/#p{page}" for page in range(51)]


def singleCraw(url):
    for line in urls:
        resp = requests.get(line)
        print(line, len(resp.text))


singleCraw(urls)
end = time.time()
print("单线程耗时:", end - start)


def getOneRequest(url):
    resp = requests.get(url)
    print(url, len(resp.text))

start = time.time()
threds = list()
for line in urls:
    threds.append(threading.Thread(target=getOneRequest, args=(line,)))

for thred in threds:
    thred.start()

for thred in threds:
    thred.join()
end = time.time()
print("多线程耗时:", end - start)

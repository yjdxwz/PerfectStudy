import time
import threading
from threading import Lock,RLock

threads = []

alock = Lock()
a = 0


def shangke():
    time.sleep(2)
    global a
    with alock:
        a += 1


for i in range(10):  # 启动10个线程
    sk = threading.Thread(target=shangke)
    sk.start()
    threads.append(sk)

for line in threads:
    line.join()
print(threading.activeCount())
print(a)
# threading.activeCount():#查看当前运行的线程数，包括主线程



# echo "# LexianghuiBackend" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M master
# git remote add origin git@github.com:yjdxwz/PerfectStudy.git
# git push -u origin master
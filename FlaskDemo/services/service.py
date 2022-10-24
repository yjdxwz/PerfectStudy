from concurrent.futures import ThreadPoolExecutor
import time
import sys
from threading import Lock
import random
import threading
from threading import Thread
ThPool = ThreadPoolExecutor(max_workers=3,thread_name_prefix="test")
taskLock = Lock()

# 用于控制线程执行
allTaskCommit = list()


# 用于显示线程执行结果
allTaskRsult = list()






def CheckA():
    time.sleep(20)

    print()
    print(f"线程名：{threading.current_thread().name}+ 运行了 {sys._getframe().f_code.co_name} 函数,{threading.get_native_id}")
    return f"result {sys._getframe().f_code.co_name}"


def CheckB():
    time.sleep(random.randint(1, 3))
    print(f"线程名：{threading.current_thread().name} 运行了 {sys._getframe().f_code.co_name} 函数,{threading.get_native_id}")
    return f"result {sys._getframe().f_code.co_name}"


def CheckC():
    time.sleep(random.randint(1, 3))
    print(f"线程名：{threading.current_thread().name} 运行了 {sys._getframe().f_code.co_name} 函数,{threading.get_native_id}")
    return f"result {sys._getframe().f_code.co_name}"


def CheckD():
    time.sleep(random.randint(1, 3))
    print(f"线程名：{threading.current_thread().name} 运行了 {sys._getframe().f_code.co_name} 函数,{threading.get_native_id}")
    return f"result {sys._getframe().f_code.co_name}"


def CheckE():
    time.sleep(random.randint(1, 3))

    print(f"线程名：{threading.current_thread().name} 运行了 {sys._getframe().f_code.co_name} 函数,{threading.get_native_id}")
    return f"result {sys._getframe().f_code.co_name}"


def exec(func):
    func()


#

def execTask():
    ThPool = ThreadPoolExecutor(max_workers=3, thread_name_prefix="test")

    global allTaskRsult
    for line in [allTaskCommit,allTaskRsult]:
        line.append(ThPool.submit(CheckA))
        line.append(ThPool.submit(CheckB))
        line.append(ThPool.submit(CheckC))
        line.append(ThPool.submit(CheckD))
        line.append(ThPool.submit(CheckE))
    allTaskRsult = list(set(allTaskRsult))


def getTaskCount():
    for feature in allTaskCommit:
        if feature.done():
            allTaskCommit.remove(feature)
    return len(
        allTaskCommit
    )


def shutDownALlTask():
    for feature in allTaskCommit:
        if not feature.done():
            ThPool.shutdown()
    return str(getTaskCount())
def execStatus():
    taskCount = getTaskCount()
    print(f"线程数{taskCount}")
    if taskCount:
        return f"<p>当前已经存在执行任务，请稍后。。。线程数：{taskCount}</p>"
    else:
        execTask()
        return f"<p>多任务执行已启动</p>"




def getResultTask():
    result = "空的"
    for feature in allTaskRsult:
        if feature.done():
            result += feature.result()
        else:
            result +=f"{feature} 还没有执行完\n"
    return result

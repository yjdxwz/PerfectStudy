'''线程池：concurrent.futures主线程想获取子线程状态，返回值。。。。统一了多线程和多进程的编码格式，方便切换'''
import time
# /from

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
def runner(times):
    time.sleep(times)
    return timesexecutor = ThreadPoolExecutor( max_workers=10)  #
    task1 = executor.submit(runner,(2)) #立即返回
    # done用于判断任务是否完成
    # print(task1.done())#
    # \result可以用于获取返回结果#
    # print(task1.result())#
    # task2.cancel()取消没运行的任务# 需求：获取已经成功的返回time_list = [2,3,4,5,3,2]# 方法一：那个先处理完打印那个all_task = [executor.submit(runner,(t)) for t in time_list]for task in all_task:#按执行的数据打印返回结果    print(task.result())for task in as_completed(all_task): #那个先完成打印那个    print(task.result())#方法二：通过excutor获取完成的task，打印顺序和time_list顺序一致# for data in executor.map(runner,time_list):#     print(data)分享：0喜欢
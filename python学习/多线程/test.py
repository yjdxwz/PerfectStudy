from concurrent.futures import ProcessPoolExecutor

import os, time,random

executor = ProcessPoolExecutor(max_workers=3)

futures=[]
def task(n):
    print('%s is runing' %os.getpid())

    time.sleep(random.randint(1,3))
    return n**2


for i in range(11):
    executor.__dir__()
    future=executor.submit(task,i)
    futures.append(future)
executor.shutdown(True)
print('+++>')
for future in futures:
    print(future.result())



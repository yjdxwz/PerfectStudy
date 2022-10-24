from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import threading
pool = ThreadPoolExecutor(max_workers=5,thread_name_prefix="aaa")
def th():
    print(threading.current_thread().name +'_______'+str(threading.current_thread().native_id))
    print()


pool.submit(th())
pool.submit(th())
pool.submit(th())




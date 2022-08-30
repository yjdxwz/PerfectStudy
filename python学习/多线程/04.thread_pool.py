import concurrent.futures
import SingleThread

# craw


with concurrent.futures.ThreadPoolExecutor() as pool:
    # 这个htmls 是线程执行的结果
    # 需要把 urls 这个参数提前准备好
    # map的结果 和入参 是顺序对应的
    htmls = pool.map(SingleThread.getCrow, SingleThread.urls)

    htmls = list(zip(SingleThread.urls, htmls))
    # 获取结果
    for url, html in htmls:
        print(url, len(html))

# pool = concurrent.futures.ThreadPoolExecutor()

# parse
with concurrent.futures.ThreadPoolExecutor(thread_name_prefix="nipanbo") as pool:
    futures = {}
    # with 中可以使用 变量htmls
    for url, html in htmls:
        varaaa = pool._threads

        feture = pool.submit(SingleThread.parse, html)
        futures[feture] = url
    # as_completed 哪个任务先完成就先返回哪个, 顺序是不固定的
    for feture in concurrent.futures.as_completed(futures):
        url = futures[feture]
        print(url, feture.result())


    print(pool)
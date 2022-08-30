import asyncio
import time
import aiohttp
import SingleThread

semaphore = asyncio.Semaphore(10)


async def async_craw(url):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                result = await resp.text()
                await asyncio.sleep(5)
                print(f"craw URL  {url},{len(result)}")


loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(async_craw(url))
    for url in SingleThread.urls
]
start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()

print(f"携程执行完毕花费时间{end - start}s")

# 控制并发度
# 携程执行完毕花费时间30.462027072906494s

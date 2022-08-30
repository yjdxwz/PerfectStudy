import time

import requests
from bs4 import BeautifulSoup

urls = [f"https://www.cnblogs.com/#p{line}" for line in range(59)]


def getCrow(url):
    r = requests.get(url)
    return r.text


def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.getText()) for link in links]


if __name__ == "__main__":
    start = time.time()
    for line in urls:
        print(parse(getCrow(line)))
    end = time.time()

    print(f"单线程爬虫时间耗费{end - start}s")
# 单线程爬虫时间耗费5.997749090194702s

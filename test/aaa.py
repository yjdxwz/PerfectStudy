import requests

# cookie_info = 'your cookiedata'
# cookie_list = [info.strip().split('=') for info in cookie_info.split(';')]
# cookies = {data[0]: data[1].replace('"', '') for data in cookie_list}
url = 'https://www.douban.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
}
session = requests.session()  # 创建session对象
# requests.utils.add_dict_to_cookiejar(session.cookies, cookies)  # 将cookie信息存入cookiejar对象中
res = session.get(url, headers=headers).content.decode()  # 进行请求
print(res)

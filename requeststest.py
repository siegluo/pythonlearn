# *-* coding:utf-8 *-*
import re

import chardet
import requests
from bs4 import BeautifulSoup

# r = requests.get('http://www.baidu.com')
# print(r.encoding)
# char = chardet.detect(r.content)
# print(char)
# char = chardet.detect(r.content)['encoding']
# print(char)
# str = requests.get('http://www.baidu.com', stream=True)
# print(str.raw.read(10))
# b = BeautifulSoup(r.content, "lxml")
# p = b.prettify()
# print(p)


headers = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Authorization': 'Basic eXVkYW95dWFubWE6eWR5bTEwMjQ=',
           'Connection': 'keep-alive',
           'Cookie': '_ga=GA1.2.42644783.1543913309; Hm_lvt_9e70e3362807c1bd185a79655b307027=1543913309,1546481132; _gid=GA1.2.966589800.1546481132; _gat=1; Hm_lpvt_9e70e3362807c1bd185a79655b307027=1546481140; Hm_lvt_8a0e6ede16424b5310cf2f09adb4e82b=1543914332,1546481162; Hm_lpvt_8a0e6ede16424b5310cf2f09adb4e82b=1546481162',
           'Host': 'svip.iocoder.cn',
           'Referer': 'http://svip.iocoder.cn/',
           'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
           }
base_url = 'http://svip.iocoder.cn'
r = requests.get('http://svip.iocoder.cn/', headers=headers)
chardet.detect(r.content)
# print(r.text)
# bea = BeautifulSoup(r.content, 'lxml', from_encoding='utf-8')
# print(bea.prettify())
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())


# print(soup)
# html = etree.HTML(str(soup))
# urls = html.xpath(".//*[@class='header-menu']/@href")
# print(urls)


a = soup.findAll(attrs={"class": "header-menu"})
r = re.compile(r'href=\"(.*)\">(.+)</a')
urls = []
for b in a:
    ress = re.findall(r, str(b))
    if ress:
        for res in ress:
            if res:
                urls.append(res)
urls = list(set(urls))
new_urls = {}
for url in urls:
    new_url = base_url + url[0]
    new_urls[new_url] = url[1]

print(new_urls)

# headers = {'Accept': '*/*',
#            'Accept-Encoding': 'gzip, deflate',
#            'Accept-Language': 'zh-CN,zh;q=0.9',
#            'Connection': 'keep-alive',
#            'Host': 'svip.iocoder.cn',
#            'Referer': 'http://svip.iocoder.cn/',
#            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
#            }
# s = requests.Session()
# datas = {'name': 'yudaoyuanma', 'password': 'ydym1024'}
# re = s.get(url='http://svip.iocoder.cn', headers=headers)
# cook = re.cookies
# r = s.post('http://svip.iocoder.cn', cookies=cook, data=datas, headers=headers)
# chardet.detect(r.content)
# bea = BeautifulSoup(r.content, 'lxml')
# print(bea.prettify())

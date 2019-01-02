# *-* coding:utf-8 *-*
import chardet
import requests

r = requests.get('http://www.baidu.com')
print(r.encoding)
char = chardet.detect(r.content)
print(char)
char = chardet.detect(r.content)['encoding']
print(char)

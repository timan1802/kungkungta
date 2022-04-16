import requests
from bs4 import BeautifulSoup as bs
import urllib.request

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
}

# url = "https://ko.dict.naver.com/api3/koko/search?m=pc&range=all&lang=ko&hid=164989540318634560&query=" + "%EC%9D%B4%3F%3F"
url = 'https://ko.dict.naver.com/api3/koko/search?m=pc&range=all&lang=ko&hid=164989540318634560&query=%EC%9D%B4%3F%3F'
print(url)
# from urllib.request import urlopen
# import json
# httpResponse = urlopen(url)
# jsondata = json.load(httpResponse)
# print(jsondata)

# 자바스크립트 axios와 동일하게, get, post 할 수 있다.
# params = {'code': 'CRIX.UPBIT.KRW-BTC', 'count': 2,
#           'to': '2020-06-08T10:07:11Z', 'timestamp': 1591610834813}
r = requests.get(url, headers=headers)
print(r.content)
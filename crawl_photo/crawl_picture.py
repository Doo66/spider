from time import time
from threading import Thread

import requests

# 继承Thread类创建自定义的线程类
class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self._url = url
    
    def run(self):
        # 获取图片名
        filename = self._url[self._url.rfind('/') + 1:]
        resp = requests.get(self._url)
        with open("photo/" + filename, 'wb') as f:
            f.write(resp.content)

def main():
    resp = requests.get('http://api.tianapi.com/meinv/?key=1f89fcbf6f91d3ed2abea0b098482d0c&num=30')
    data_model =  resp.json()
    print(data_model)
    for mm_dict in data_model['newslist']:
        # 获取图片链接
        url = mm_dict['picUrl']
        # 利用多线程下载图片
        DownloadHanlder(url).start()

if __name__ == "__main__":
    main()
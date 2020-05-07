import requests

if __name__ == '__main__':
    target = "http://fanyi.baidu.com/"
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    #print(req.text)

    # 创建一个文件 req_text.txt
    fo = open("req_text.txt", "w")
    # 将爬取到的信息写入文件
    fo.write(req.text);
    # 关闭文件
    fo.close()

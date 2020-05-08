import requests # 爬虫
from tqdm import tqdm # 进度条
from bs4 import BeautifulSoup # 解析提取的内容

# 提取内容
def get_content(target):
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    # 使用beautifulsoup库，解析html
    bf = BeautifulSoup(html, 'lxml')
    # 小说内容在属性为content的div标签下
    # 提取小说内容
    texts = bf.find('div', id='content')
    # 跳过开头有四个空格
    content = texts.text.strip().split('\xa0'*4)
    return content

if __name__ == '__main__':
    server = 'https://www.xsbiquge.com'
    book_name = '诡秘之主.txt'
    target = 'https://www.xsbiquge.com/15_15338/'  
    # 发起请求
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    # 提取每一章节的url
    chapters = chapter_bs.find('div', id='list')
    chapters = chapters.find_all('a')
    # 提取每一章的内容
    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        # 拼接每一章节的url
        url = server + chapter.get('href')
        # 提取小说内容
        content = get_content(url)
        # 写入文件中
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')

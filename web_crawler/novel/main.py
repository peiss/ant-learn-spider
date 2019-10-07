import requests
from bs4 import BeautifulSoup

"""
代码功能：爬取一本小说，按章节存入本地的txt文件
"""

def get_novel_chapters():
    """
    爬取小说目录页，得到每个章节的链接和标题
    """
    root_url = "http://www.89wxw.cn/0_9/"
    # 使用requests下载网页，就这么一行代码
    r = requests.get(root_url)
    # 发现页面的编码不是utf8，所以这里做下编码设置
    r.encoding="gbk"
    # 进入soup进行解析
    soup = BeautifulSoup(r.text, "html.parser")
    data = []
    for dd in soup.find_all("dd"):
        link = dd.find("a")
        if not link: continue
        # 分析得到每个链接的URL和标题，因为抓取下来的地址不带域名，所以加上
        data.append(("http://www.89wxw.cn%s"%link['href'], link.get_text()))
    return data

def get_chapter_content(url):
    """
    抓取某一章节的正文文本
    """
    # requests获取小说页面HTML
    r = requests.get(url)
    # 设置编码
    r.encoding='gbk'
    # bs4解析
    soup = BeautifulSoup(r.text, "html.parser")
    # 提取content的文本，即小说的正文
    return soup.find("div", id='content').get_text()

# 获取章节列表
novel_chapters = get_novel_chapters()
# 计算总章节数目，便于查看进度
total_cnt = len(novel_chapters)
idx = 0
for chapter in novel_chapters:
    idx += 1
    print(idx, total_cnt)
    url, title = chapter
    # 写出到本地文件
    with open("%s.txt"%title, "w") as fout:
        fout.write(get_chapter_content(url))

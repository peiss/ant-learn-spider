import requests
from bs4 import BeautifulSoup
import re

crawed_imgs = set()


def get_html_urls():
    url = "https://www.5442tu.com/mingxing/"
    r = requests.get(url)
    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all("a", href=re.compile(r"//www.5442tu.com/mingxing/\d+/\d+.html"))
    urls = []
    for link in links:
        urls.append("https:" + link['href'])
    return urls


def craw_html(fname, url):
    r = requests.get(url)
    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text, "html.parser")
    img_url = soup.find("div", class_="arcBody").find("p").find("img").get("src")
    if img_url not in crawed_imgs:
        print("爬取图片：" + img_url)
        download_img(fname, img_url)
        crawed_imgs.add(img_url)


def download_img(fname, img_url):
    headers = {
        "Referer": "https://www.5442tu.com/mingxing/20190531/90026.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    r = requests.get(img_url, headers=headers)

    with open("%s.jpg" % fname, "wb") as fout:
        fout.write(r.content)


idx = 0
for url in get_html_urls():
    idx += 1
    # print(url)
    craw_html(str(idx), url)
# download_img("1", "https://pic.antns.com/2014/1202/02/01.jpg")

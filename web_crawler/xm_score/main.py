from urllib.parse import urlencode

import requests

url = "http://life.httpcn.com/xingming.asp"


def get_score(xing, ming):
    data = {
        "data_type": 0,
        "year": 1980,
        "month": 3,
        "day": 29,
        "hour": 20,
        "minute": 20,
        "pid": "北京".encode("gb2312"),
        "cid": "北京".encode("gb2312"),
        "wxxy": 0,
        "xishen": "金".encode("gb2312"),
        "yongshen": "金".encode("gb2312"),
        "xing": xing.encode("gb2312"),
        "ming": ming.encode("gb2312"),
        "sex": 1,
        "act": "submit",
        "isbz": 1
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    r = requests.get(url, data=urlencode(data), headers=headers)

    # print(r.status_code)
    r.encoding = "gb2312"

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")

    divs = soup.find_all("div", class_="chaxun_b")
    bazi, wuge = 0, 0
    for div in divs:
        if "姓名五格评分" not in div.get_text():
            continue
        fonts = div.find_all("font")
        bazi = fonts[0].get_text().replace("分", "").strip()
        wuge = fonts[1].get_text().replace("分", "").strip()
    return "%s%s" % (xing, ming), bazi, wuge


with open("input.txt") as fin, open("output.txt", "w") as fout:
    for line in fin:
        line = line.strip()
        xingming, bazi, wuge = get_score("裴", line)
        print("爬虫名字打分：%s, 八字分数：%s，五格分数：%s" % (xingming, str(bazi), str(wuge)))
        fout.write("%s\t%s\t%s\n" % (xingming, bazi, wuge))
        fout.flush()

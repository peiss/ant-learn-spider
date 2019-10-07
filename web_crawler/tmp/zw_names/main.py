from urllib.parse import urlencode

url = "http://life.httpcn.com/xingming.asp"

import requests


def get_socres(name):
    data = {
        "data_type": 0,
        "year": 1980,
        "month": 3,
        "day": 29,
        "hour": 20,
        "minute": 20,
        "pid": "北京".encode("gb2312"),
        "cid": "北京".encode("gb2312"),
        "zty": 1,
        "wxxy": 0,
        "xishen": "金".encode("gb2312"),
        "yongshen": "金".encode("gb2312"),
        "xing": "裴".encode("gb2312"),
        "ming": name.encode("gb2312"),
        "sex": 1,
        "act": "submit",
        "isbz": 1
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    r = requests.post(url, data=urlencode(data), headers=headers)
    print(r.status_code)
    r.encoding = 'gb2312'

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")

    datas = soup.find_all("div", class_="chaxun_b")
    bazi, wuge = 0, 0
    for data in datas:
        if "姓名五格评分" not in data.get_text():
            continue
        scores = data.find_all("font")
        bazi = scores[0].get_text().replace("分", "").strip()
        wuge = scores[1].get_text().replace("分", "").strip()
    return name, bazi, wuge


with open("input.txt") as fin, open("output.txt", "w") as fout:
    for line in fin:
        line = line.strip()
        name, bazi, wuge = get_socres(line)
        fout.write("%s\t%s\t%s\n" % (name, bazi, wuge))

import json

import requests
import time
import random
from urllib.parse import quote

fout = open("lagou_python.txt", "w")
keys = ["positionId", "positionName", "companyId", "companyFullName",
            "companyShortName", "industryField", "financeStage",
            "companySize", "salary", "workYear", "education"]
fout.write("\t".join([str(x) for x in keys]) + "\n")

def craw(pages):
    city = quote("北京")
    # 主url
    url1 = f"https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
    # ajax请求
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
    # 请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': f"https://www.lagou.com/jobs/list_python?px=default&city={city}",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Host': 'www.lagou.com'
    }
    # 通过data来控制翻页

    for page in range(1, 1 + pages):
        data = {
            'first': 'false',
            'pn': page,
            'kd': 'python'
        }
        s = requests.Session()  # 建立session

        # 先请求这个URL，获取cookie
        s.get(url=url1, headers=headers, timeout=3)
        cookie = s.cookies  # 获取cookie

        # 用cookie提交json请求
        r = s.post(url=url, headers=headers,
                   data=data, cookies=cookie, timeout=3)
        time.sleep(random.randint(1, 3))
        print("craw", page, r.status_code)
        parse_detial(r.content.decode("utf-8"))

        fout.flush()
    fout.close()


def parse_detial(data_json):
    data_json = json.loads(data_json)
    positions = data_json["content"]["positionResult"]["result"]

    for position in positions:
        data = [position[key] for key in keys]
        print(data)
        fout.write("\t".join([str(x) for x in data]) + "\n")


craw(24)
fout.flush()
fout.close()

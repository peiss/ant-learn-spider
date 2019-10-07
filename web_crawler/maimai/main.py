import requests
import requests.cookies
import json
import time

cookie_jar = requests.cookies.RequestsCookieJar()

with open("cookie.txt") as fin:
    cookiejson = json.loads(fin.read())
    for cookie in cookiejson:
        cookie_jar.set(
            name=cookie["name"],
            value=cookie["value"],
            domain=cookie["domain"],
            path=cookie["path"]
        )

url = "https://maimai.cn/sdk/web/gossip_list?u=1515483&channel=www&version=4.0.0&_csrf=lJp5jIru-z0wYKBjcA-jX49ZeagslbCryxdM&access_token=1.e0640697ab7f42f399a32c830eb9097e&uid=%22O3xXrmQGCYTkKBCGmz%2FLp%2FAirs3A3wL6ApgZu%2Fo1crA%3D%22&token=%22%2BNnjV%2BFR9jcrlzfU4fl22Znjrwbf4AU0N8SOULlWvMDKFYyF2ioxb5QlTYQAv5et8CKuzcDfAvoCmBm7%2BjVysA%3D%3D%22&page={idx}&jsononly=1"
for idx in range(10):
    time.sleep(1)
    print("**爬取脉脉匿名列表：第%d页" % idx)
    r = requests.get(url.format(idx=idx), cookies=cookie_jar)
    resultjson = json.loads(r.text)
    print(resultjson)
    for data in resultjson["data"]:
        if "text" not in data:
            continue
        print(data["text"])

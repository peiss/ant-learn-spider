import requests
from bs4 import BeautifulSoup

for idx in range(200):
    print("#"*30, idx+1)

    url = "https://www.cnblogs.com/mvc/AggSite/PostList.aspx"

    data = {"CategoryType":"SiteHome",
            "ParentCategoryId":0,
            "CategoryId":808,
            "PageIndex":idx+1,
            "TotalPostCount":4000,
            "ItemListActionName":"PostList"}
    r = requests.post(url, data=data)
    if r.status_code!=200:
        raise Exception()
    soup = BeautifulSoup(r.text, "html.parser")

    post_items = soup.find_all("div", class_="post_item")
    for post_item in post_items:
        link = post_item.find("a", class_="titlelnk")
        digg = post_item.find("span", class_="diggnum")
        print(link["href"], link.get_text(), digg.get_text())

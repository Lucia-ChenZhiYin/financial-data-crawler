import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

import time

url ="https://www.ptt.cc/bbs/Stock/index.html"
#抓取網址
my_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"}
#偽裝一般瀏覽器
data_list = []
#將寫成Json檔案
for page in range(3):
    #寫入三頁面
    response = requests.get(url, headers = my_headers)
    #'get'做出與瀏覽器一樣動作以向伺服器拿資料，'request抓取網頁給BeautifulSoup解析
    soup = BeautifulSoup(response.text,"html.parser")

    articles = soup.find_all("div",class_="r-ent")

    for a in articles:
    #迴圈將一頁面的文章寫入
        data = {}
        title = a.find("div",class_="title")
        if title and title.a:
            title = title.a.text
        else:
            title = "無標題"
        data["標題"] = title

        popular = a.find("div",class_="nrec")
        if popular and popular.span:
            popular = popular.span.text
        else:
            popular = "N/A"
        data["人氣"] = popular

        date = a.find("div",class_="date")
        if date:
            date = date.text
        else:
            date = "N/A"
        data["日期"] = date
        data_list.append(data)

    prev_button = soup.find("a", string="‹ 上頁")
    #叫BeautifulSoup在網頁找文字"< 上頁"的<a>標籤
    #print(f"測試，按鈕物件為:{prev_button}")

    if prev_button:
        url = "https://www.ptt.cc"+prev_button["href"]
    else:
        break
    #更新url變數，將後半段網址拼接上PPT官方網域
    time.sleep(2)
    #休息避免被當作惡意攻擊

with open("ppt_Stock_data.json","w", encoding="utf-8") as file:
#"with" 可以用於自動close，檔名，寫入，字體，
    json.dump(data_list, file, ensure_ascii=False, indent=4)
#"dump" 自動轉化list成符合JSON標準格式字串，維持中文原型，縮排四格
print("這是股票PTT爬蟲測試Json")

df = pd.DataFrame(data_list)
df.to_excel("ppt_Stock_data.xlsx", index=False, engine="openpyxl")
print("這是股票PTT爬蟲測試Pandas")
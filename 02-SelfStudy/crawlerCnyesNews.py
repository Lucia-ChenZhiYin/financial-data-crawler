import requests
import pandas as pd
from datetime import datetime
import time
from bs4 import BeautifulSoup
import html

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'
}
news_list = []
startPage = 1
endPage = 2
for page in range(startPage, endPage+1):
    url = f"https://api.cnyes.com/media/api/v1/newslist/category/tw_stock?page={page}&limit=30&showOutsource=1"
#使用f-string可以把page的變數變動帶入網址
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        news_items = data['items']['data']
        
        for item in news_items:
            pubTime = datetime.fromtimestamp(item['publishAt']).strftime('%Y-%m-%d %H:%M')
            title = item['title']
            news_id = item['newsId']
            news_url = f"https://news.cnyes.com/news/id/{news_id}"

            raw_content = item.get('content') or item.get('summary') or ''
            decoded_content = html.unescape(raw_content)
            clean_content = BeautifulSoup(decoded_content, 'html.parser').get_text()
            clean_content = clean_content.replace('\n', ' ').strip()
            #使用BeautifulSoup清理HTML標籤只留文字，
            if clean_content:
                summary = clean_content[:20].strip() + "..."
                #切片語法，取前120字
            else:
                summary = "無內文"
            news_list.append([pubTime, title, summary, news_url])

        print(f"目前存取第{page}頁，已累積{len(news_list)}筆新聞")
    else:
        print("無法存取網頁")

    time.sleep(1)

df = pd.DataFrame(news_list, columns=["發布時間", "新聞標題","新聞摘要", "新聞連結"])
df.to_excel('cnyes_tw_stock_news.xlsx', index=False, engine="openpyxl")
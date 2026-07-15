import requests
from bs4 import BeautifulSoup
import os


def download_img(url, save_path):
    print(f"正在下載圖片:{url}")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    with open(save_path, 'wb') as file:
        file.write(response.content)

    print(f"下載回傳的資料大小為: {len(response.content)} bytes")
    # 檢查：回傳內容的前 100 個字元，確定是否真的下載下圖片
    print(f"檔案前 100 個字元內容為:\n{response.content[:100]}")

    print("-" * 30)

def main():

    url = "https://www.ptt.cc/bbs/KoreaStar/M.1762785630.A.C12.html"
    
    headers = {"User_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Cookie":"over18=1"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")
    #print(soup.prettify())

    spans = soup.find_all("span", class_="article-meta-value")
    title = spans[2].text.strip()

    #1.建立圖片資料夾
    dir_name = f"image/{title}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    #'dirs'資料夾

    #2.找到網頁所有圖片
    links = soup.find_all("a")
    allow_file = ["jpg", "png", "jpeg", "gif"]
    for link in links:
        href = link.get("href")
        if not href:
            continue
        file_name = href.split("/")[-1]
        extension = href.split(".")[-1].lower()
        #print(extension)
        if extension in allow_file:
            print(f"檔案型態:{extension}")
            print(f"url: {href}")
            download_img(href, f"{dir_name}/{file_name}")

        #print(href)
if __name__ == "__main__":
    main()

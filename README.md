# financial-data-crawler
>課程參考 :【Python 爬蟲 】2 小時初學者課程 ：一次學會 PTT 爬蟲、Hahow 爬蟲、Yahoo 電影爬蟲！

---

##開發環境與工具

| 項目 | 配置內容 |
| :--- | :--- |
| **作業系統** | Window |
| **開發工具** | Visual Studio Code(VScode) |
| **程式語言** | Python 3.13.9 |

###主要套件
    * `requests`(網路請求發送)
    * `beautifulsoup4`(HTML網頁標籤解析)
    * `json`(簡單資料交換格式儲存)
    * `pandas` & `openpyxl`(Excel資料處理與匯出)
    


##日誌
###階段一:環境準備與確認
-[x]python3 環境安裝 確認
-[x]設定VSCode的Python開發擴充套件
-[x]確認Requests可正常運作

***階段二:PPT靜態網頁爬蟲實作
-[x]處理反爬蟲機制，利用headers，帶入 User-Agent，將 Python 請求偽裝成一般瀏覽器
-[x]資料持久化儲存，使用'with open'語法，將網頁原始碼本地儲存成HTML
-[x]導入'BeautifulSoup'解析'div.r-ent'等標籤，提取{標題,人氣,日期}等欄位
-[x]使用"Json"匯出成'ppt_nba_data.json'
-[x]使用"Pandas"匯出成'ppt_nba_data.xlsx'試算表

***階段三:金融相關數據與統計分析(改寫目標)
-[x]切換至股票(Stock)板PPT進行爬取
-[x]增加自動翻頁功能跨頁面抓取歷史資料
    -*遇到問題*:網頁中的'‹'為特殊符號，經測試回傳僅有'None'回傳
    -*已處理*
-[x]將"time.sleep(1)"改為"time.sleep(2)"避免網站阻擋
-[x]成功匯出三頁面的股票版"ppt_Stock_data.json","ppt_Stock_data.xlsx"檔案



        
        
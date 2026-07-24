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

- [x] python3 環境安裝 確認
- [x] 設定VSCode的Python開發擴充套件
- [x] 確認Requests可正常運作

###階段二:PPT靜態網頁爬蟲實作(`crawlerJson.py & crawlerPandas.py`)

- [x] 處理反爬蟲機制，利用`headers`，帶入 User-Agent，將 Python 請求偽裝成一般瀏覽器
- [x] 資料持久化儲存，使用`with open`語法，將網頁原始碼本地儲存成HTML
- [x] 導入`BeautifulSoup`解析`div.r-ent`等標籤，提取{標題,人氣,日期}等欄位
- [x] 使用"Json"匯出成`ppt_nba_data.json`
- [x] 使用"Pandas"匯出成`ppt_nba_data.xlsx`試算表

###階段三:金融相關數據與統計分析，增加功能與改變目標網站(crawlerStock.py)

- [x] 切換至股票(Stock)板PPT進行爬取
- [x] 增加自動翻頁功能跨頁面抓取歷史資料
    * *遇到問題* : 網頁中的'‹'為特殊符號，經測試回傳僅有`None`回傳
    * *已處理* : 沒處理無法翻頁
- [x] 將`time.sleep(1)`改為`time.sleep(2)`避免網站阻擋
- [x] 成功匯出三頁面的股票版`ppt_Stock_data.json`,`ppt_Stock_data.xlsx`檔案

###階段四:PTT下載圖片實作(crawlerBeauty.py)

- [x] 使用 `BeautifulSoup` 的 `find_all`功能找到文章標題作為資料夾檔名
- [x] 檔案系統與路經自動化處理(os模組)
    * 使用 `os.path.exists()` 自動判斷目標路徑是否已存在。
    * 使用 `os.makedirs()` 將文章圖片歸檔
- [x] 找出網頁中所有的超連結，並且規範白名單只下載四種圖片格式("jpg", "png", "jpeg", "gif")
    * 用split("/")切割網址，[-1]找最後一個元素為檔名，例如:abc1234.jpg
    * 用spilt(".")切割網址，[-1].lower()加上強制轉換小寫，找到.jpg
- [x] 呼叫download_img函式帶入href,儲存路徑(資料夾檔名/圖片檔名)
- [] 成功下載可存取圖片
    *遇到問題* : 開啟下載圖片無內容

###階段五:PPT下載圖片實作，功能改善(crawlerKoreaStar.py)

- [x] 圖片下載與處理防禦機制實作:
    * *遇到問題* : 0 Bytes異常，在下載函數中補上`headers`宣告，不要放cookie
    * *已處理* : 影片無特別提及，經測試確認
    * *遇到問題* : 無法正確提取標題名導致資料夾建立時命名路徑衝突，使用 `.strip()`去除首尾隱性空格
    * *已處理* : 影片無特別提及，經測試確認
- [x] 成功提取網站全部圖片並存檔在獨立資料夾

###階段六:進行Ajax爬蟲(crawlerHahow.py)

- [x] 分析 Hahow 網站載入機制，了解瀏覽器發送 Ajax 請求後，伺服器回傳 JSON 資料並經由前端 JavaScript 進行動態渲染的過程
- [x] 繞過前端 HTML 結構，直接對 Hahow 後端 API 發送 HTTP 請求，並將獲取之 JSON 資料解析並轉換為 Python 字典格式
- [x] 從字典中提取目標課程資訊（如課程名稱、價格、預購人數、評價）
- [x] 使用 `pandas.DataFrame` 建立結構化資料表並定義明確所需欄位名稱
- [x] 將整理後的課程數據自動匯出為 `course.xlsx` 試算表，完成動態數據擷取與歸檔

###階段七:改變目標網站為台股新聞，爬取CnyesNews(crawlerCnyesNews.py)

- [x] **多頁面 Ajax API 批次數據抓取**：
  * 分析鉅亨網（cnyes）台股新聞載入機制，運用 `f-string` 動態構建分頁 URL，實現跨頁面（`page` 參數）資料擷取
  * 導入 `time.sleep()` 建立請求頻率限制，落實禮貌爬蟲機制。
- [x] **時間戳記 (Timestamp) 解析與格式轉換**：
  * 解析 API 回傳之 `publishAt` Unix 時間戳記，使用 `datetime.fromtimestamp()` 將其轉換為易讀的日期格式 (`YYYY-MM-DD HH:MM`)
- [x] **新聞摘要提取與資料清洗 (Data Cleaning)**：
  * HTML 轉義字元解碼：使用 `html.unescape()` 將 API 內文中的轉義標籤（如 `&lt;p&gt;`）還原為標準 HTML 格式
  * 純文字剝離與裁切：搭配 `BeautifulSoup('html.parser')` 剝除所有 HTML 標籤，並進行空格清理與前 120 字切片處理，自動生成乾淨的新聞摘要
- [x] **API 結構分析與爬蟲效能重構 (Refactoring)**：
  * *遇到問題*：遇到 JSON 結構（`items -> data -> [0]`）及 `KeyError` 異常。
  * *已處理*：觀察 API 回傳之完整 JSON 結構後發現，列表層級 API 已包含 `content` 與 `summary` 欄位
- [x] **自動化數據匯出**：
  * 使用 `pandas` 將發布時間、新聞標題、120 字新聞摘要與新聞連結整理為結構化表格，並匯出為 `cnyes_tw_stock_news.xlsx` 試算表。


        
        
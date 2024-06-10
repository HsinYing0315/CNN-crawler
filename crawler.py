import requests
from bs4 import BeautifulSoup

def fetch_article(url):
# 發送 GET 請求取得網頁內容
    response = requests.get(url)

    # 檢查請求是否成功
    if response.status_code == 200:
        # 解析 HTML 內容
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 找出網頁標題
        paragraphs = soup.find_all('p', class_='paragraph')
        
        article = {
            'title': soup.title.string,
            'paragraph': '\n'.join(paragraph.get_text(strip=True) for paragraph in paragraphs)
        }
        return article
    else:
        return (f"無法取得網頁內容，狀態碼：{response.status_code}")

import requests
from bs4 import BeautifulSoup

# 요청 헤더 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

# Daum 뉴스 페이지 URL
url = "https://news.daum.net"

# 요청 보내기
req = requests.get(url, headers=headers)

# 인코딩 설정 (자동 감지 또는 강제 UTF-8 설정)
req.encoding = req.apparent_encoding  # 자동 감지
# req.encoding = 'utf-8'  # 강제 UTF-8 설정 (필요하면 주석 해제)

# HTML 파싱
soup = BeautifulSoup(req.text, "html.parser")

# 기사 목록 선택
item_newsbasic = soup.select(".item_newsbasic")

# 언론사 정보 출력
for cont in item_newsbasic:
    #  press = cont.select(".txt_info")[1]["span"] 
    press=cont.select_one(".con_txt > span ").text
    link=cont["href"]
    
    cont_tumb=cont.select_one(".tit_txt").text
    print(f"{press} - {cont_tumb}")
    print(link)
    print()

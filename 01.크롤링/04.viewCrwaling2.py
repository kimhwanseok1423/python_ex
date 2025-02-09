import requests
from bs4 import BeautifulSoup

base_url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
keyword=input("검색어를 입력하세요 : ")
url=base_url+keyword



#print(url)
headers= {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}


req=requests.get(url,headers=headers)

html=req.text

soup=BeautifulSoup(html,"html.parser")

# 인기글 작성자 , 제목 가져오기
total_area=soup.select(".view_wrap")
timeline_area=soup.select(".bx")


if total_area:
    areas=total_area
elif timeline_area:
    areas=timeline_area
else:
    print("확인필요")

for area in areas : 
    title=area.select_one(".title_link")
    name=area.select_one(".user_info")
    print(name.text)
    print(title.text)
    print(title["href"])
    print()

print(len(areas))
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
titles=soup.select(".title_link")
names=soup.select(".user_info")
#print(result)
for result in zip(names,titles) : 
    #print(result['href'])
   
    print(result[0].text)
    print(result[1].text)
    print(result[1]['href'])
    print()


 #    
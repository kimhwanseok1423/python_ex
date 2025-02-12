import requests
from bs4 import BeautifulSoup

url="https://www.ssg.com/event/eventMain.ssg"


# 요청 헤더 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

req=requests.get(url,headers=headers)
html=req.text

soup=BeautifulSoup(html,"html.parser")

evt_osmu_lst=soup.select_one(".evt_osmu_lst")
eo_link=evt_osmu_lst.select(".eo_link")

for unit in eo_link : 
    link=unit["href"]
    if link.startswith("http") :
        print(link)
    else:
        print(f"https://event.ssg.com{link}")
    
    eo_in=unit.select_one(".eo_in")

    text_list=eo_in.find_all(string=True)
    # print(text_list)
    # print()
    for text in text_list : 
        if text != "\n":
            print(text)
    print()

    

import requests
from bs4 import BeautifulSoup

url="https://weather.naver.com/"



headers= {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}


req=requests.get(url,headers=headers)

html=req.text

soup=BeautifulSoup(html,"html.parser")
# print(soup.h1)
# print()

# h1=soup.find('h1') 
# print(h1)
# print()

# h1=soup.select_one('h1')
# print(h1)
# print()


# h1=soup.find(class_="search_logo")
# print(h1)
# print()

# h1=soup.find(id="special-input-logo")
# print(h1)
# print()


# menu=soup.find(class_="menu",string="미세먼지")
# print(menu)
# print()


# menu=soup.find("a",string="미세먼지")
# print(menu.text)
# print(menu["href"])
# print()

menus=soup.find_all(class_="menu")
#print(menus)
#print(len(menus))
for menu in menus:
    print(menu.text)
    print("https://weather.naver.com"+menu['href'])
    print()
import requests
from bs4 import BeautifulSoup

url="https://startcoding.pythonanywhere.com/basic"

req=requests.get(url)


html=req.text
# print(html)
  
soup=BeautifulSoup(html,"html.parser")

logo=soup.select_one(".service_name").text
print(logo)
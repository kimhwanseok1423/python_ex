import requests
from bs4 import BeautifulSoup

url="https://www.naver.com/"

headers= {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}


req=requests.get(url,headers=headers)
# user agent
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 

 # print(req.raise_for_status)
# 결과값 200 잘됐다는 의미


print(req.request.headers)
#print(req.request)


html=req.text






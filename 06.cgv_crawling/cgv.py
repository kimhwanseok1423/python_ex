import requests
from bs4 import BeautifulSoup

url="http://www.cgv.co.kr/movies/?lt=1&ft=0"

headers={
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

req=requests.get(url,headers=headers)
html=req.text
soup=BeautifulSoup(html,"html.parser")

sect_movie_chart=soup.select_one(".sect-movie-chart")

movie_chart=sect_movie_chart.select("li")
#print(len(movie_chart))

for rank,movie in enumerate(movie_chart,1) :
    title=movie.select_one(".title")
    score=movie.select_one(".percent")
    egg_gage=movie.select_one(".egg-gage.small > .percent")
    info=movie.select_one(".txt-info > strong").next_element

    print(f"<<<{rank}>>>")
    print(title.text)
    print(score.get_text(" : "))
    print(egg_gage.text)
   # print(info.text.strip())
    #print(info.strip())
    print(f"{info.strip()} 개봉")

    print()
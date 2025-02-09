import requests
from bs4 import BeautifulSoup

song_num_text= "javascript:melon.link.goAlbumDetail('11647670');"

def get_song_nums(song_num_text):
    # song_num= []
    # for num in song_num_text:
    #     if num.isdigit():
    #         song_num.append(num)
    # song_num= "".join(song_num)

    # return song_num
   song_num= "".join([num for num in song_num_text if num.isdigit()])
   return song_num



url="https://www.melon.com/chart/index.htm"





headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}
req=requests.get(url,headers=headers)
html=req.text





soup=BeautifulSoup(html,"html.parser")
# lst50=soup.select(".lst50")
# lst100=soup.select(".lst100")
# lst=lst50+lst100

# lst=soup.select(".lst50, .lst100")  

# #중에 다됨 경우의수 여러개 보여주기위해 
lst=soup.find_all(class_=["lst50", "lst100"])

for rank ,i in enumerate(lst,1):
    title=i.select_one(".ellipsis.rank01 a")

    singer=i.select_one(".ellipsis.rank02 > a")
    singer_link=get_song_nums(singer["href"])
    album=i.select_one(".ellipsis.rank03 > a")
    album_link=get_song_nums(album["href"])
    print(f"{rank} : {title.text}")
    print(f"{singer.text} : https://www.melon.com/artist/timeline.htm?artistId={singer_link}")
    print(f"{album.text} : https://www.melon.com/album/detail.htm?albumId={album_link}")
    print()
   
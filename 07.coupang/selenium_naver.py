from selenium import webdriver
from bs4 import BeautifulSoup
import time
base_url="https://search.naver.com/search.naver?ssc=tab.influencer.chl&where=influencer&sm=tab_jum&query="
keyword=input("검색어를 입력하세요 : ")
url=base_url+keyword



driver=webdriver.Chrome()
driver.get(url)
time.sleep(3)

driver.execute_script("window.scrollTo(0,2000)")
time.sleep(2)


html=driver.page_source




soup=BeautifulSoup(html,"html.parser")

# 인기글 작성자 , 제목 가져오기
total_area=soup.select(".keyword_box_wrap.type_color")



if total_area:
    areas=total_area
else:
    print("확인필요")

for area in areas: 
    title = area.select_one(".title_area")  # <a> 태그 포함
    title_link=area.select_one(".title_area > a")
    name = area.select_one(".user_info")

    if name:
        print(name.text.strip())  # name이 있을 경우 출력
    else:
        print("이름 없음")

    if title:
        print(title.text)  # 제목 출력
        print(title_link["href"])  # 링크 출력
    else:
        print("제목 없음")
        print("링크 없음")

    print()

print(f"총 {len(areas)}개의 결과를 가져왔습니다.")
print(f"총 {len(areas)}개의 결과를 가져왔습니다.")
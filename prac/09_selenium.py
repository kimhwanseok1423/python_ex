from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

user_data=r"D:\bc_study\web python\prac\datalog"
options=Options()


## 화면 안꺼짐 이거있으면
options.add_experimental_option("detach",True)

## user agent의 크롬버전을 낮추거나 바꾸고싶을때 user_agent에서 버전만 낮추고 실행시 개발자 도구에서 적용된 버전으로 실행됨
options.add_argument(f"user-agemt={user_agent}")
options.add_argument(f"user-data-dir={user_data}")


## 실행시 최대 크기로 실행
options.add_argument("--start-maximized")

## 실행시 전체화면으로 실행
## options.add_argument("--start-fullscreen")

## 실행시 윈도우 사이즈 사용자에 맞게 조절해서도 가능함
##.add_argument("window-size=500,500")

# 실행시 화면창 안열고 사용할경우 쓰임
# options.add_argument("--headless")
# 실행시 화면창 안열고 사용할경우 쓰임 (만약 위에꺼 써도 안되면 이것도 써보기)
# options.add_argument("--disable-gpu")

#음소거 모드 설정시 (유튜브 자동실행되서 불편하거나 할떄 쓰면됨)
options.add_argument("--mute-audio")
# 시크릿모드
# options.add_argument("incognito")

#시크릿모드에서 첫 알림 팝업창 제거하기 , 불필요한 메시지 제거 옵션
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])



service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=options)

url="http://naver.com"
driver.get(url)

print(driver.page_source[:1000])
# driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"


options=Options()


## 화면 안꺼짐 이거있으면
options.add_experimental_option("detach",True)

## user agent의 크롬버전을 낮추거나 바꾸고싶을때 user_agent에서 버전만 낮추고 실행시 개발자 도구에서 적용된 버전으로 실행됨
options.add_argument(f"user-agemt={user_agent}")


## 실행시 최대 크기로 실행
options.add_argument("--start-maximized")

## 실행시 전체화면으로 실행
## options.add_argument("--start-fullscreen")

## 실행시 윈도우 사이즈 사용자에 맞게 조절해서도 가능함
##.add_argument("window-size=500,500")



service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=options)

url="http://naver.com"
driver.get(url)
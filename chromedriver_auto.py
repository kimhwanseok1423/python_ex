from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

## 셀레니움 할때 가져와야하는것

service=Service(ChromeDriverManager().install())

## 크롬 드라이브를 자동설치하는 드라이브를 만들었다고 이해하기


driver=webdriver.Chrome(service=service)

driver.get("https://google.com")
time.sleep(2)

## --------------           -----------------------
## 셀레니움 업그레이드법  pip install --upgrade selenium

## 셀레니움 자동업그레이드 방식이 아닌 최근에는 이런식으로 셀레니움 업그레이드를하면 코드를 줄일수있음.
## service 사용할필요없이 이것만쓰면됨  (이런느낌으로 import후 가져오면됨)
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://google.com")
time.sleep(2)



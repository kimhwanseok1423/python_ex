from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome WebDriver 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 띄우지 않고 실행
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36")

# WebDriver 실행
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 쿠팡 홈페이지 접속
base_url = "https://www.coupang.com/np/search?component=&q="

keyword=input("검색할 삼품을 입력하세요 : ")
search_url=base_url+keyword
driver.get(search_url)

time.sleep(3)

names = driver.find_elements(By.CSS_SELECTOR, "[class=search-product]")

for name in names:
    print(name["class"])
# WebDriver 종료
driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# 설치된 ChromeDriver 경로와 버전 확인
print(ChromeDriverManager().install())
options=Options()

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=options)

url="https://naver.com"

driver.get(url)